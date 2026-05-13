# coding: utf-8

from parties.scanner import barcode_reader
import os
import re
import csv
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import logging

class Command(BaseCommand):
    help = "Scan_job_command."

    def add_arguments(self, parser):
        parser.add_argument('bool', nargs='?', default=False)
        parser.add_argument('filebrowserfilename', nargs='?', default='')

    def handle(self, *args, **options):
        bool = options['bool']
        filebrowser_file_name = options['filebrowser_file_name']
        
        if not bool:
            raise CommandError('<bool> must be a bool.')
        else:
            self.stdout.write('START\n')

            
            file_out = os.path.join(
                settings.MEDIA_ROOT, filebrowser_file_name)

            with open(file_out, mode='w', newline='') as file_out:
                try:
                    while True:
                        print("tsert: ", filebrowser_file_name)
                        # scanned_code = barcode_reader()
                        # if scanned_code:
                            # file_out.write(scanned_code + "\n")
                            # file_out.flush()
                            # print(f"Сохранено: {scanned_code}")
                        break
                except KeyboardInterrupt:
                    logging.debug('Keyboard interrupt')
                except Exception as err:
                    logging.error(err)

            
        
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
