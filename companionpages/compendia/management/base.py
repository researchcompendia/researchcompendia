"""
Base classes for compendia management commands
"""
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from compendia import choices


class BaseArticleCommand(BaseCommand):
    args = '[<id id...>]'

    statuses = [status[0] for status in choices.STATUS]

    option_list = BaseCommand.option_list + (
        make_option(
            '-a',
            '--all',
            action='store_true',
            dest='all',
            default=False,
            help='apply command to all articles (status and IDs are ignored)',
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
            help='apply command to articles of the requested status. (IDs are ignored).'
                    + ' Valid choices: %s.' % statuses,
        ),
    )

    def handle(self, *args, **options):
        if options['all']:
            self.handle_all()
        elif options['status'] is not None:
            self.handle_status(options['status'])
        elif len(args) > 0:
            self.handle_selected(args)
        else:
            raise CommandError('missing required options for migrate_tags command')

    def handle_all(self):
        raise NotImplementedError('subclasses of BaseArticleCommand must provide a handle_all() method')

    def handle_status(self, status):
        raise NotImplementedError('subclasses of BaseArticleCommand must provide a handle_status() method')

    def handle_selected(self, id_list):
        raise NotImplementedError('subclasses of BaseArticleCommand must provide a handle_selected() method')
