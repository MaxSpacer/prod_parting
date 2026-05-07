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

@receiver(post_save, sender=Party)
def get_scan(sender, instance, created, **kwargs):
    if instance.status:
        print(...)

        file_out = os.path.join(
            settings.MEDIA_ROOT, instance.report_party_file)
        
        with open(file_out, "w"):
            pass
        
        if file_out:
            with open(file_out, mode='w', newline='') as file_out:
                row_writer = csv.writer(file_out, delimiter=';')
                
                try:
                    while True:
                        upcnumber = barcode_reader()
                        row_writer.writerow(upcnumber)
                        print('test -', upcnumber)
                except KeyboardInterrupt:
                    logging.debug('Keyboard interrupt')
                except Exception as err:
                    logging.error(err)
            
        
    # if created:
    #     context = {
	# 	    'contact_name': instance.customer_name,
	# 	    'callme_number': instance.id,
	# 	    'contact_phone': instance.customer_phone,
	# 	}
    #     subject = 'Заказ звонка № call-%s' % instance.id
    #     html_message = render_to_string('mail_templates/mail_callme_template.html', context)
    #     plain_message = strip_tags(html_message)
    #     from_email = 'info@dohaich.ru'
    #     to = 'zakaz@dohaich.ru'
    #     # print(instance.is_emailed)
    #     if instance.is_emailed == False:
    #         if subject and html_message and from_email:
    #             try:
    #                 if send_mail(subject, plain_message, from_email, [to], html_message=html_message):
    #                     Callmecontact.objects.filter(pk=instance.pk).update(is_emailed=True)
    #                     instance.is_emailed = True
    #                     # print(instance.is_emailed)

    #             except BadHeaderError:
    #                 print('Invalid header found in email %s' % instance.id)
    #             # return HttpResponse('Invalid header found %s' % instance.id)
    #             # education_order.is_emailed = True
    #             return HttpResponse('sended')
    #         else:
    # 	        return print('Make sure all fields are entered and valid %s' % instance.id)
