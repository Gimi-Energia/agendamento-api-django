# Generated by Django 4.0.6 on 2022-07-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0005_alter_sala_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='empresa',
            field=models.CharField(choices=[('Gimi', 'Gimi'), ('GPB', 'GBP'), ('GBL', 'GBL'), ('GS', 'GS')], default='Gimi', max_length=100, verbose_name='Empresa'),
            preserve_default=False,
        ),
    ]
