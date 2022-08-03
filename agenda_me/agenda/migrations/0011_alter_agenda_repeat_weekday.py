# Generated by Django 4.0.6 on 2022-07-27 12:34

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0010_agenda_repeat_agenda_repeat_weekday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='repeat_weekday',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'segunda-feira'), (1, 'terça-feira'), (2, 'quarta-feira'), (3, 'quinta-feira'), (4, 'sexta-feira'), (5, 'sábado')], max_length=1, null=True, verbose_name='Dias que se repete'),
        ),
    ]
