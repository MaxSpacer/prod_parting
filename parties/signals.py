# -*- coding: utf-8 -*-

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.dispatch import receiver
from django.db.models.signals import post_save

from parties.daemon import testdaemon
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
# from crontab import CronTab
from .tasks import scan_job
from django.core import management 
 
 
 
import sys,time

 
@receiver(post_save, sender=Party)
def get_scan(sender, instance, created, **kwargs):
    daemon = testdaemon()
    if instance.status:
        ...
        # daemon.start()
        # scan_job.enqueue(str(instance.report_party_file.path_full))
        # my_cron = CronTab(user='max_spacer')

        # job = my_cron.new(command=f'/home/max_spacer/prod_parting/.venv/bin/python /home/max_spacer/prod_parting/manage.py scan_job_command 0 {instance.report_party_file}', comment='scan_job')
        # job.setall('*/10 * * * * *')
        # for jo in my_cron:
        #     print(jo)    
        # my_cron.write()
    # else:
        # daemon.stop()
    #     from django_tasks_db.models import DBTaskResult

        # # Delete all tasks with a specific name/function
        # Task.objects.filter(task_name="your_task_function_name").delete()

        # Or delete everything in the queue
        # dbt = DBTaskResult.objects.all()
        # for t in dbt:
        #     t.status = "SUCCESSFUL"
        #     t.save()
        # Source - https://stackoverflow.com/a/907743

        # from django.core.management import call_command

        # management.call_command('db_worker', '--no-reload')


        # Source - https://stackoverflow.com/a/3777308
        # Posted by Manoj Govindan, modified by community. See post 'Timeline' for change history
        # Retrieved 2026-05-14, License - CC BY-SA 4.0

        # import subprocess
        # subprocess.call(['python', './test.sh']) # Thanks @Jim Dennis for suggesting the []
  
        # Source - https://stackoverflow.com/a/26625982
# Posted by Medhat, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-15, License - CC BY-SA 3.0

        import subprocess
        cmd = '/home/max_spacer/prod_parting/.venv/bin/python /home/max_spacer/prod_parting/parties/daemon.py start'

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate() 
        result = out.split('\n')
        for lin in result:
            if not lin.startswith('#'):
                print(lin)

