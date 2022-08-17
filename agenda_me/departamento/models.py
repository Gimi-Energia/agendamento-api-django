from django.db import models

from agenda_me.utils import EMPRESAS

class Department(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="nome")
    company = models.CharField(max_length=255, default=EMPRESAS.GIMI, choices=EMPRESAS.CHOICES, null=True, blank=False, verbose_name="empresa")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
