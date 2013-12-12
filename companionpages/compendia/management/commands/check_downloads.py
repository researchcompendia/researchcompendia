from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from compendia import choices
from compendia import tasks


"""

check file download availability for Articles.

start celery::

    celery -A companionpages worker --loglevel=info

run command, for example::

    ./manage.py check_downloads 123

"""


class Command(BaseCommand):
    args = '[<id id...>]'
    help = 'Checks the optionally specified articles for file availability'

    statuses = [status[0] for status in choices.STATUS]

    option_list = BaseCommand.option_list + (
        make_option(
            '-a',
            '--all',
            action='store_true',
            dest='all',
            default=False,
            help='Check file availability for all articles (status and IDs are ignored)',
        ),
        make_option(
            '-s',
            '--status',
            dest='status',
            type='choice',
            choices=statuses,
            action='store',
            default=None,
            metavar='STATUS',
            help='Check file availability for articles of the requested status. (IDs are ignored).'
                    + ' Valid choices: %s.' % statuses,
        ),
    )

    def handle(self, *args, **options):
        if options['all']:
            tasks.check_all_article_downloads.delay()
        elif options['status'] is not None:
            tasks.check_selected_status_article_downloads.delay(options['status'])
        elif len(args) > 0:
            tasks.check_selected_article_downloads.delay(args)
        else:
            raise CommandError('missing required options for check_downloads command')
