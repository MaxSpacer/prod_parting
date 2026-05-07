# coding: utf-8

from parties.scanner import barcode_reader
import os
import re
import csv
# import libusb_package
import usb
# from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


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

            import logging

            # if __name__ == '__main__':
        
            try:
                while True:
                    upcnumber = barcode_reader()
                    print(upcnumber,  'test')
            except KeyboardInterrupt:
                logging.debug('Keyboard interrupt')
            except Exception as err:
                logging.error(err)

            # os.environ['PYUSB_DEBUG'] = 'debug'
        # import usb.core
        # usb.core.find()
        # # with pure PyUSB
        # for dev in usb.core.find(find_all=True):
        #     print('dev')
        #     print(dev)
            
            
        self.stdout.write('STOP\n')
