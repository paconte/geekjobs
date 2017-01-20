from django.core.management.base import BaseCommand
from geekjobs.stackoverflow_parser import download_stackoverflow_jobs
from geekjobs.stackoverflow_parser import stackoverflow_json_file


class Command(BaseCommand):
    help = 'Download and parse stackoverflow jobs.'

    def handle(self, *args, **options):
        download_stackoverflow_jobs()
        self.stdout.write(self.style.SUCCESS('Jobs successfully parsed in to file: "%s"' % stackoverflow_json_file))
