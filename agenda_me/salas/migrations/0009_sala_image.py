# Generated by Django 4.0.6 on 2022-08-08 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0008_alter_sala_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/sala/img', verbose_name='Imagem'),
        ),
    ]
