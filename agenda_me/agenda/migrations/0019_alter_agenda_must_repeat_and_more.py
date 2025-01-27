# Generated by Django 4.0.6 on 2022-08-03 14:26

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0018_agenda_must_repeat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='must_repeat',
            field=models.BooleanField(blank=True, default=False, verbose_name='Reunião se repete?'),
        ),
        migrations.AlterField(
            model_name='periodicagenda',
            name='repeat_weekday',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(None, 'nenhum'), (0, 'segunda-feira'), (1, 'terça-feira'), (2, 'quarta-feira'), (3, 'quinta-feira'), (4, 'sexta-feira'), (5, 'sábado')], max_length=11, null=True, verbose_name='Dias que se repete'),
        ),
    ]
