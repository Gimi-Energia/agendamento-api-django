# Generated by Django 4.0.6 on 2022-08-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=254)),
                ('company', models.CharField(choices=[('GIMI', 'Gimi'), ('GPB', 'GPB'), ('GBL', 'GBL'), ('GS', 'Gimi Service')], max_length=255)),
            ],
        ),
    ]