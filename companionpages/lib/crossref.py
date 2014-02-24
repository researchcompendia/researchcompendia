#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import re
from urllib import quote

from bs4 import BeautifulSoup
import requests

logger = logging.getLogger('researchcompendia.lib')

"""
This is an unsophisticated library to parse responses from the crossref query servlet.
The crossref servlet provides unixsd which provides the publisher
content along with crossref-specific metadata.

The goal for us is to take responses from the query and map fields on to Article
and Collaborator fields. Nothing in the request or query shall cause a failure.
If there is a problem, it is indicated in the dict.

References

CrossRef query service

* http://help.crossref.org/#using_http

CrossRef unixsd help and schema

* http://help.crossref.org/#unixsd
* http://www.crossref.org/schemas/crossref_query_output3.0.xsd

Publishers return information in unixref1.0 or unixref1.1.

* http://doi.crossref.org/schemas/unixref1.1.xsd
* http://doi.crossref.org/schemas/unixref1.0.xsd
"""


def query(pid, doi_param, timeout=1.0):
    """ returns a dictionary optionally populated with Article and Collaborator attributes

    pid: a validated username for the crossref query service
    doi: a doi query string from the client
    timeout: time in seconds that we are willing to wait for an answer. default is 800 milliseconds.

    exceptions: no exception or error from this call should affect the client.
    It catches problems and moves on.

    response fields

    msg: a message about the request.
      * 'invalid doi parameter' indicates an error due to caller passing a bad parameter
      * 'crossref requests exception' indicates an error due to network timeout, etc.
      * 'crossref exception' indicates a non 2xx response from crossref service
      * 'crossref error' indicates a missing query or status
      * 'crossref status' indicates a status other than 'resolved'
      * 'ok' indicates everything is excellent

    status: an http status code
    compendia: a dict of fields corresponding to Article and Collaborators
    unixsd: raw format from crossref response
    """

    try:
        doi = match_doi(doi_param)
    except TypeError:
        msg = 'invalid doi parameter: %s' % doi_param
        logger.warning(msg)
        return {'msg': msg, 'status': 400}

    if doi == '':
        msg = 'invalid doi parameter: %s' % doi_param
        logger.warning(msg)
        return {'msg': msg, 'status': 400}

    try:
        r = requests.get('http://doi.crossref.org/servlet/query', params={
            'pid': pid,
            'noredirect': True,
            'id': doi,
            'format': 'unixsd', },
            #timeout=timeout
        )
    except requests.exceptions.RequestException:
        logger.warning('crossref requests exception', exc_info=True)
        return {'msg': 'requests exception', 'status': 500}

    if not r.ok:
        logger.warning('crossref exception %s', r)
        return {'msg': 'crossref exception', 'status': r.status_code, 'xml': r.text}

    response = {'msg': 'ok', 'status': r.status_code, 'doi': doi}

    logger.debug(quote(r.content))
    response.update(parse_crossref_output(r.content))
    return response


def parse_crossref_output(xml):
    # I'm using 'xml' instead of 'lxml' because 'lxml' ignores CDATA,
    # but 'xml' turns CDATA in to text elements
    soup = BeautifulSoup(xml, 'xml')

    # the response is a query that has a resolve status
    if soup.query is None:
        return {'msg': 'crossref error'}
    if 'status' not in soup.query.attrs:
        return {'mgs': 'crossref error'}
    if soup.query['status'] != 'resolved':
        return {'mgs': 'crossref status %s' % (soup.query['status'])}
    if soup.doi_record is None:
        return {'msg': 'crossref missing doi_record'}

    compendia = parse_doi_record(soup)
    logger.debug('compendia %s', compendia)
    return {'compendia': compendia}


def parse_doi_record(soup):
    result = {}

    if soup.resource is not None:
        result['article_url'] = soup.resource.text
    if soup.title is not None:
        result['title'] = soup.title.text

    result.update(parse_contributors(soup))
    result.update(parse_doi_type(soup))
    return result


def parse_doi_type(soup):
    # crossref has a lot of types, we'll just handle a few at first
    doi_type = ''
    if soup.doi is not None:
        doi_type = soup.doi.attrs.get('type', '')

    # oh boy a messy lookup table and we can clean this up later
    parser_lookup = {
        'conference_paper': parse_conference_paper,
        'journal_article': parse_journal_article,
    }
    parser = parser_lookup.get(doi_type, parse_journal_article)
    results = parser(soup)
    logging.debug('parse_doi_type %s', results)
    return results


def parse_conference_paper(soup):
    if soup.proceedings_title is not None:
        return {'journal': soup.proceedings_title.text}
    return {}


def parse_journal_article(soup):
    result = {}

    if soup.full_title is not None:
        result['journal'] = soup.full_title.text
    if soup.month is not None:
        result['month'] = soup.month.text
    if soup.year is not None:
        result['year'] = soup.year.text
    if soup.volume is not None:
        result['volume'] = soup.volume.text
    if soup.issue is not None:
        result['issue'] = soup.issue.text
        result['number'] = soup.issue.text
    if soup.first_page is not None:
        pages = soup.first_page.text
        if soup.last_page is not None:
            endash = u'\u2013'
            pages = u'%s%s%s' % (pages, endash, soup.last_page.text)
        result['pages'] = pages
    if soup.journal_article is not None and 'publication_type' in soup.journal_article.attrs:
        result['publication_type'] = soup.journal_article['publication_type']
    return result


def parse_contributors(soup):
    collaborators = []
    names = []
    for contributor in soup.find_all('person_name'):
        person = parse_person(contributor)
        collaborators.append(person)
        names.append(parse_name(person))
    authortext = ', '.join([name for name in names if name != ' '])
    return {'collaborators': collaborators, 'authortext': authortext}


def parse_name(person):
    return ' '.join([person.get('given_name', ''), person.get('surname', '')])


def parse_person(contributor):
    person = {}
    if contributor.given_name is not None:
        person['given_name'] = contributor.given_name.text
    if contributor.surname is not None:
        person['surname'] = contributor.surname.text
    if 'sequence' in contributor.attrs and contributor['sequence'] == 'first':
        person['author_order'] = 0
    if contributor.ORCID is not None:
        person['orcid'] = contributor.ORCID.text
    if contributor.affiliation is not None:
        person['affiliation'] = contributor.affiliation.text
    #TODO if 'contributor_role' in contributor.attrs:
    #   we could see about making our model have roles rather than coder, author.
    #   it makes more sense.
    return person


def match_doi(query):
    """ match doi from query """
    match = re.search(r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>])\S)+)\b', query)
    if match is None:
        logger.debug('Nothing for query %s', query)
        return ""
    result = match.group(0)
    logger.debug('query: %s result: %s', query, result)
    return result


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('doi', help='well-formed DOI for query')
    parser.add_argument('--pid', help='crossref account')
    parser.add_argument('--timeout', default=0.8, type=float, help='requests timeout')
    args = parser.parse_args()
    r = query(args.pid, args.doi, timeout=args.timeout)
    print(r)
