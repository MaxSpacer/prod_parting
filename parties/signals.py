# -*- coding: utf-8 -*-

from django.dispatch import receiver
from django.db.models.signals import post_save
from parties.daemon import testdaemon
from .models import Party
import subprocess

 
@receiver(post_save, sender=Party)
def get_scan(sender, instance, created, **kwargs):
    daemon = testdaemon()
    if instance.status:
        cmd = f'/home/max_spacer/prod_parting/.venv/bin/python /home/max_spacer/prod_parting/parties/daemon.py start {instance.report_party_file.path_full}'

    else:
        cmd = '/home/max_spacer/prod_parting/.venv/bin/python /home/max_spacer/prod_parting/parties/daemon.py stop'

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate() 
    result = str(out).split('\n')
    for lin in result:
        if not lin.startswith('#'):
            print(lin)

