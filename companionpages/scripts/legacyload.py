#!/usr/bin/env python

import argparse
import json
import os
from collections import defaultdict


"""
This reads a results json file that was created by the
https://github.com/codersquid/rmcscrape scraper. This adds records as
apropriate You need to have this in the same directory as manage.py to run
this.

NOTE: I inserted 3 "new_key" fields in the json that was output from the scraper.
because the URLs from our prerelease database environment were given out to be
put in documents. I needed to script those pk's by hand.

* article keys from prerelease database environment, legacy keys
* 36, 190
* 54, 303
* 49, 265

results from the scrape have the following keys

"coders": dictionary of coder dictionaries keyed by name
"authors": dictionary of author dictionaries keyed by name
"article_url": optional url string
"names": list of strings of authors
"legacy_id": int from old system
"title": string
"abstract": abstract of article
"journal": string
"explanatory_text": abstract of code and data

coder and author dicts can have the following keys

"affiliation": optional string (only was available in the scraped data for coders)
"country": optional string (only was available in the scraped data for coders)
"coder": true or false
"author": true or false
"last": last name
"first": first name

"""


def save_articles(scrapes, site_owner):
    for scrape in scrapes:
        coders = scrape.get('coders', {})
        article_url = scrape.get('article_url', '')
        authors = scrape.get('authors', {})
        legacy_id = scrape.get('legacy_id')
        new_key = scrape.get('new_key', '')
        title = scrape.get('title', '')
        abstract = scrape.get('abstract', '')
        journal = scrape.get('journal', '')
        explanatory_text = scrape.get('explanatory_text', '')

        # merge authors and coders.
        authorship = defaultdict(dict)
        for k in coders:
            authorship[k].update(coders[k])
        for k in authors:
            authorship[k].update(authors[k])

        author_string = ", ".join(authors.keys())
        coder_string = ", ".join(coders.keys())

        author_text = author_string
        if coder_string != '':
            author_text += '\nCoders: %s' % coder_string

        if new_key != '':
            pk = int(new_key)
        else:
            pk = int(legacy_id)

        article = models.Article(
            id=pk,
            site_owner=site_owner,
            status=STATUS.active,
            authors_text=author_text,
            authorship=json.dumps(authorship),
            title=title,
            paper_abstract=abstract,
            code_data_abstract=explanatory_text,
            journal=journal,
            legacy_id=legacy_id,
            article_url=article_url,
            notes_for_staff="legacy",
        )
        article.save()


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "companionpages.settings")
    from compendia import models
    from compendia.choices import STATUS
    from users.models import User

    parser = argparse.ArgumentParser(description="""
    This reads a scrape json file that was created by the
    https://github.com/codersquid/rmcscrape scraper and adds article records to
    the db. You need to be in the same directory as manage.py to run this.
    """)

    #parser.add_argument('--collaborators', type=file, help='a json file with collaborators.')
    parser.add_argument('--scrapes', type=file, help='a json file with scraped legacy data.')
    args = parser.parse_args()

    if args.scrapes is not None:
        print("loading scrapes...")
        scrapes = json.load(args.scrapes)
        site_owner = User.objects.get(pk=1)
        save_articles(scrapes, site_owner)
