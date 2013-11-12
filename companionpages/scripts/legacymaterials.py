#!/usr/bin/env python

import argparse
import os

# flake8: noqa

"""
This scans a directory containing directories numbered according to the legacy id
of the articles. Each numbered directory contains files from the old site.

"""

def get_all_legacy_articles():
    articles = models.Article.objects.filter(
        legacy_id__isnull=False
    )
    return articles


def get_legacy_articles(legacy_ids=[]):
    articles = models.Article.objects.filter(
        legacy_id__in=legacy_ids
    )
    return articles


def get_filehandles(path, legacy_id):
    fullpath = os.path.join(path, legacy_id)
    if not os.path.exists(fullpath) or not os.path.isdir(fullpath):
        return []
    fnames =  os.listdir(fullpath)

    return fnames

def get_tags(fh):
    tags = []
    for tag in fh:
        tags.append(tag)
    return tags
        


def save_material(articles, path, dryrun=False):
    print('handling articles')
    too_big = 2048**3
    for article in articles:
        legacy_id = str(article.legacy_id)
        print('%s article %s' % (legacy_id, article))

        fullpath = os.path.join(path, legacy_id)
        if not os.path.exists(fullpath) or not os.path.isdir(fullpath):
            print('%s    %s is not a valid directory' % (legacy_id, fullpath))
            continue
        filenames = os.listdir(fullpath)
        print('%s    handling path %s files %s' % (legacy_id, fullpath, filenames))

        for filename in filenames:
            filepath = os.path.join(fullpath, filename)
            if os.path.isdir(filepath):
                print('%s    skipping subdirectory %s' % (legacy_id, filepath))
                continue
            filestat = os.stat(filepath)
            if filestat.st_size > too_big:
                print('%s    skipping file %s is too big %s' % (legacy_id, filepath, filestat.st_size))
                continue
            with open(filepath) as fh:
                # add some logic here so that we decide which field to use
                # code_archive_file
                # data_archive_file
                # tags

                if filename.startswith(('data', 'Data')):
                    print('%s    handling %s as %s' % (legacy_id, filename, 'data'))
                    if dryrun is False:
                        article.data_archive_file.save(filename, ContentFile(fh.read()),)
                elif filename.startswith('tag'):
                    tags = get_tags(fh)
                    if len(tags) > 0:
                        if dryrun is False:
                            article.tags.add(*tags)
                else:
                    print('%s    handling %s as %s' % (legacy_id, filename, 'code'))
                    if dryrun is False:
                        article.code_archive_file.save(filename, ContentFile(fh.read()),)
        print('%s done' % legacy_id)


    print('done handling articles')


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "companionpages.settings")
    from django.conf import settings
    from compendia import models
    from django.core.files.base import ContentFile

    parser = argparse.ArgumentParser(description="""
        For each article with a legacy id, this scans a directory that contains files from the old site,
        creates supplemental materials for each files, and adds these to the article record.
    """)

    parser.add_argument('legacy_ids', metavar='N', nargs='*',
        help='legacy ids. use to run against specific articles')
    parser.add_argument('--path', default='/home/sheila/notetoself/scraped/',
        help='path to directory of legacy file directories')
    parser.add_argument('--dryrun', action='store_true')
    args = parser.parse_args()
    print args.dryrun
    if len(args.legacy_ids) > 0:
        print 'legacy_ids: ', args.legacy_ids
        articles = get_legacy_articles(args.legacy_ids)
    else:
        print 'all'
        articles = get_all_legacy_articles()
    save_material(articles, args.path, args.dryrun)
