# Generated by Django 4.0.6 on 2022-08-18 18:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0025_alter_agenda_titulo_alter_periodicagenda_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='created_by',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(limit_value=4)], verbose_name='Seu nome'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='titulo',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(limit_value=4)], verbose_name='Assunto'),
        ),
        migrations.AlterField(
            model_name='periodicagenda',
            name='created_by',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(limit_value=4)], verbose_name='Seu nome'),
        ),
        migrations.AlterField(
            model_name='periodicagenda',
            name='titulo',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(limit_value=4)], verbose_name='Assunto'),
        ),
    ]
