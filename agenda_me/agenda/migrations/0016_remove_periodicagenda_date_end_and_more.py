# Generated by Django 4.0.6 on 2022-07-28 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0015_remove_agenda_last_same_item_remove_agenda_repeat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodicagenda',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='periodicagenda',
            name='date_init',
        ),
    ]
