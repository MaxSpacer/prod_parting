from django.db import models
from filebrowser.fields import FileBrowseField

# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from django.template.defaultfilters import slugify
import uuid


class Party(models.Model):
    def def_file_name():
        return str(f"{uuid.uuid4()}") + '.csv'

    platform_number = models.PositiveIntegerField(blank=False, null=True, default=1)
    is_emailed = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    report_party_file = FileBrowseField(max_length=250, extensions=['.csv'], blank=False, null=True, default=def_file_name)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # def save(self, *args, **kwargs):
    #     self.report_party_file = f"{uuid.uuid4()}" + 't.csv'

    #     super(Party, self).save(*args, **kwargs)

    # Source - https://stackoverflow.com/a/6462188
# Posted by Bernhard Vallant, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-07, License - CC BY-SA 3.0

    # @receiver(pre_save)
    # def my_callback(sender, instance, *args, **kwargs):
    #     print('ff')
    #     instance.report_party_file = str(instance.id) + 't.csv'

# class PartyItem(models.Model):
#     party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
#     datamatrix_string = models.CharField(max_length=128, blank=False, null=True)
#     created = models.DateTimeField(auto_now_add=True , auto_now=False)
