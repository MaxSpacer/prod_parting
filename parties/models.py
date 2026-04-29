from django.db import models


class Party(models.Model):
    platform_number = models.PositiveIntegerField(blank=False, null=True, default=1)
    is_emailed = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

class PartyItem(models.Model):
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    datamatrix_string = models.CharField(max_length=128, blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)