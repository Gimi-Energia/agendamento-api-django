# Generated by Django 4.0.6 on 2022-08-17 13:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0023_alter_agenda_titulo_alter_periodicagenda_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='created_by',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(limit_value=4)], verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='titulo',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(limit_value=8)], verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='periodicagenda',
            name='created_by',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(limit_value=4)], verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='periodicagenda',
            name='titulo',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(limit_value=8)], verbose_name='Título'),
        ),
    ]