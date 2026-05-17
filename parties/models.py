from django.db import models
from filebrowser.fields import FileBrowseField
from django.core.exceptions import ValidationError
import uuid


class Party(models.Model):
    def def_file_name():
        return str(f"{uuid.uuid4()}") + '.csv'

    platform_number = models.PositiveIntegerField("номер линии", blank=False, null=True, default=1)
    is_emailed = models.BooleanField(default=False)
    status = models.BooleanField("Активен?", default=True)
    report_party_file = FileBrowseField("отчет по партии", max_length=250, extensions=['.csv'], blank=False, null=True, default=def_file_name)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    class Meta:
        verbose_name = 'Партия'
        verbose_name_plural = 'Партии'
        
    def clean(self):
        c = Party.objects.filter(status__exact=True, platform_number__exact = self.platform_number)  
        if c and self.status:
            raise ValidationError(f"На линии {self.platform_number} уже есть активные партии {tuple(c.values_list( 'id' ,flat = True))}!\nДеактивируйте их, сняв галку с поле Активен")
        
    def __str__(self):
        return f"Партия № {self.id}"   