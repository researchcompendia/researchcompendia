import logging

from bs4 import BeautifulSoup
import requests

logger = logging.getLogger(__name__)

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


def query(pid, doi, timeout=0.60):
    """ returns a dictionary optionally populated with Article and Collaborator attributes

    pid: a validated username for the crossref query service
    doi: a validated doi string
    timeout: time in seconds that we are willing to wait for an answer. default is 60 milliseconds.

    exceptions: no exception or error from this call should affect the client.
    It catches problems and moves on.

    response fields

    msg: a message about the request.
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
        r = requests.get('http://doi.crossref.org/servlet/query', params={
            'pid': pid,
            'noredirect': True,
            'id': doi,
            'format': 'unixsd', },
            timeout=timeout)
    except requests.exceptions.RequestException:
        logger.debug('crossref requests exception')
        logger.warning('crossref requests exception')
        return {'msg': 'requests exception', 'status': 500}

    if not r.ok:
        logger.warning('crossref exception %s', r)
        return {'msg': 'crossref exception', 'status': r.status_code, 'xml': r.text}

    # todo
    response = parse_crossref_output(r.text)
    return {'msg': 'ok', 'status': r.status_code, 'compendia': response, 'unixsd': r.text}


def parse_crossref_output(xml):

    soup = BeautifulSoup(xml, 'lxml')

    # the response is a query that has a resolve status
    if soup.query is None:
        return {'msg': 'crossref error'}
    if 'status' not in soup.query.attrs:
        return {'mgs': 'crossref error'}
    if soup.query['status'] != 'resolved':
        return {'mgs': 'crossref status %s' % (soup.query['status'])}

    return parse_doi_record(soup)


def parse_doi_record(soup):
    result = {}

    if soup.doi_record is None:
        return result

    if soup.doi_record.journal is None:
        return result

    result.update(parse_journal(soup))

    return result


def parse_journal(soup):
    result = {}

    if soup.full_title is not None:
        result['journal'] = soup.full_title.text
    if soup.resource is not None:
        result['article_url'] = soup.resource.text
    if soup.title is not None:
        result['title'] = soup.title.text

    if soup.journal_article is not None and 'publication_type' in soup.journal_article.attrs:
        result['publication_type'] = soup.journal_article['publication_type']

    collaborators = []
    for contributor in soup.find_all('person_name'):
        person = parse_person(contributor)
        collaborators.append(person)
    result['collaborators'] = collaborators

    return result


def parse_person(contributor):
    person = {}
    if contributor.given_name is not None:
        person['given_name'] = contributor.given_name.text
    if contributor.surname is not None:
        person['surname'] = contributor.surname.text
    if 'sequence' in contributor.attrs and contributor['sequence'] == 'first':
        person['author_order'] = 0
    #TODO if 'contributor_role' in contributor.attrs:
    #   we could see about making our model have roles rather than coder, author.
    #   it makes more sense.
    return person
