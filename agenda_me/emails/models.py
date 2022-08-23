from django.db import models

from agenda_me.utils.empresas import EMPRESAS

class Email(models.Model):
    address = models.EmailField()
    company = models.CharField(max_length=255, choices=EMPRESAS.CHOICES)

    def __str__(self):
        return f'{self.address} - {self.company}'