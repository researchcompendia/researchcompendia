#!/usr/bin/env python

import argparse
import json
import os


"""
This Reads a collaborators json file that was created by the
https://github.com/codersquid/rmcscrape scraper and adds Collaborator records
to db. You need to be in the same directory as manage.py to run this or
fix the import depth.

Save collaborators before saving scrapes. I didn't write this to do everything
once.

collaborators is a dict keyed by strings that are names.
"affiliation": optional string
"country": optional string
"coder": true or false
"author": true or false


scrapes is a dict
"coders": dictionary of coder collaborators keyed by name
"article_url": optional url string
"names": list of strings of authors
"legacy_id": int from old system
"title": string
"abstract": string
"journal": string
"explanatory_text": explanation string

"""


def save_collaborators(collaborators):
    for name, attributes in collaborators.items():
        collaborator = models.Collaborator(
            name=name,
            coder=attributes.get('coder', False),
            author=attributes.get('author', False),
            affiliation=attributes.get('affiliation', ''),
            country=attributes.get('country', ''),
        )
        collaborator.save()


def save_companionarticles(scrapes):
    for scrape in scrapes:
        coders = scrape.get('coders', {})
        article_url = scrape.get('article_url', '')
        names = scrape.get('names', [])
        legacy_id = scrape.get('legacy_id')
        title = scrape.get('title', '')
        abstract = scrape.get('abstract', '')
        journal = scrape.get('journal', '')
        explanatory_text = scrape.get('explanatory_text', '')

        # make a list of names we can use to fetch records for
        names.extend(coders.keys())
        collaborators = models.Collaborator.objects.filter(name__in=names)

        article = models.CompanionArticle(
            title=title,
            abstract=abstract,
            journal=journal,
            legacy_id=legacy_id,
            article_url=article_url,
        )
        article.save()

        article.collaborators.add(*collaborators)

        article.supportingmaterial_set.create(
            name='materials supporting %s' % (title),
            explanatory_text=explanatory_text,
        )


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'companionpages.settings')
    from supportingmaterials import models

    parser = argparse.ArgumentParser(description="""
    This Reads a collaborators json file that was created by the 
    https://github.com/codersquid/rmcscrape scraper and adds
    Collaborator records to db. You need to be in the same directory as manage.py to run this.

    Save collaborators before saving scrapes. I didn't write this to do everything
    at once.
    """)

    parser.add_argument('--collaborators', type=file, help='a json file with collaborators.')
    parser.add_argument('--scrapes', type=file, help='a json file with scraped legacy data.')
    args = parser.parse_args()

    if args.collaborators is not None:
        print("loading collaborators...")
        collaborators = json.load(args.collaborators)
        save_collaborators(collaborators)

    if args.scrapes is not None:
        print("loading scrapes...")
        scrapes = json.load(args.scrapes)
        save_companionarticles(scrapes)
