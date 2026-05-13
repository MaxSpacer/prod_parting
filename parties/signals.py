# -*- coding: utf-8 -*-

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Party
# from .models import Mainformcontact
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import get_object_or_404

import os
from django.conf import settings
import logging
from parties.scanner import barcode_reader
import csv
import time
# import asyncio
from crontab import CronTab

@receiver(post_save, sender=Party)
def get_scan(sender, instance, created, **kwargs):
    if instance.status:
        print(...)
        my_cron = CronTab(user='max_spacer')

        job = my_cron.new(command=f'/home/max_spacer/prod_parting/.venv/bin/python /home/max_spacer/prod_parting/manage.py scan_job_command 0 {instance.report_party_file}', comment='scan_job')
        for jo in my_cron:
            print(jo)    
