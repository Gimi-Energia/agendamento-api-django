# Generated by Django 4.0.6 on 2022-08-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0009_sala_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='empresa',
            field=models.CharField(choices=[('Gimi', 'gimi'), ('GPB', 'gpb'), ('GBL', 'gbl'), ('GS', 'gs')], max_length=100, verbose_name='Empresa'),
        ),
    ]