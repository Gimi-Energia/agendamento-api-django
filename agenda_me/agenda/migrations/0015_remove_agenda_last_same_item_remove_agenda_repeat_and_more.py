# Generated by Django 4.0.6 on 2022-07-28 15:31

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
        ('salas', '0005_alter_sala_name'),
        ('agenda', '0014_alter_agenda_last_same_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='last_same_item',
        ),
        migrations.RemoveField(
            model_name='agenda',
            name='repeat',
        ),
        migrations.RemoveField(
            model_name='agenda',
            name='repeat_weekday',
        ),
        migrations.CreateModel(
            name='PeriodicAgenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('date_init', models.DateTimeField(null=True, verbose_name='Data/Hora de início')),
                ('date_end', models.DateTimeField(blank=True, null=True, verbose_name='Data/Hora de término')),
                ('code', models.CharField(editable=False, max_length=255, null=True, verbose_name='Código de segurança')),
                ('created_by', models.CharField(max_length=100, verbose_name='Criado por')),
                ('creator_email', models.EmailField(max_length=254, verbose_name='Email de quem criou')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('repeat_weekday', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'segunda-feira'), (1, 'terça-feira'), (2, 'quarta-feira'), (3, 'quinta-feira'), (4, 'sexta-feira'), (5, 'sábado')], max_length=11, null=True, verbose_name='Dias que se repete')),
                ('creator_department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='departamento.department', verbose_name='Departamento de quem criou')),
                ('sala', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='salas.sala')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
