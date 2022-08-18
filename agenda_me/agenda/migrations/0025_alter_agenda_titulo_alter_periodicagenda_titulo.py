# Generated by Django 4.0.6 on 2022-08-18 17:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0024_alter_agenda_created_by_alter_agenda_titulo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='titulo',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(limit_value=4, message='TESTE')], verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='periodicagenda',
            name='titulo',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(limit_value=4, message='TESTE')], verbose_name='Título'),
        ),
    ]