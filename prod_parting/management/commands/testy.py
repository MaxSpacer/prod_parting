# coding: utf-8

# import os
# import re
# import csv
# import copy

# from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

# from bs4 import BeautifulSoup

# import requests


class Command(BaseCommand):
    help = "(Re)parse it."

    def add_arguments(self, parser):
        parser.add_argument('bool', nargs='?', default=False)

    def handle(self, *args, **options):
        bool = options['bool']

        if not bool:
            raise CommandError('<bool> must be a bool.')
        else:
            self.stdout.write('START\n')

            from parties.daemon import barcode_reader
            with open('xxx.txtp', mode='w', newline='') as file_out:
                # scan = barcode_reader()
                while True:


                    scanned_code = barcode_reader()
                    if scanned_code:
                        file_out.write(scanned_code + "\n")
                        file_out.flush()

        self.stdout.write('STOP\n')
