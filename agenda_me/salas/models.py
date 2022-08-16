from django.db import models
from agenda_me.utils import EMPRESAS


class Sala(models.Model):   
    id = models.AutoField(primary_key=True) 
    empresa = models.CharField(choices=EMPRESAS.CHOICES, max_length=100, verbose_name="Empresa")
    image = models.ImageField(upload_to='uploads/sala/img', null=True, blank=True, verbose_name='Imagem')
    name = models.CharField(max_length=255, blank=False, verbose_name="Nome")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
   
    def __str__(self):        
        return '{0}'.format(self.name)