# Generated by Django 4.0.6 on 2022-09-22 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_alter_department_company'),
        ('emails', '0002_alter_email_company'),
        ('salas', '0013_alter_sala_empresa'),
        ('agenda', '0027_agenda_company_periodicagenda_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='creator_department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='departamento.department', verbose_name='Departamento de quem criou'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agenda',
            name='creator_email',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='emails.email', verbose_name='Email de quem criou'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agenda',
            name='sala',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='salas.sala'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='periodicagenda',
            name='creator_department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='departamento.department', verbose_name='Departamento de quem criou'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='periodicagenda',
            name='creator_email',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='emails.email', verbose_name='Email de quem criou'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='periodicagenda',
            name='sala',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='salas.sala'),
            preserve_default=False,
        ),
    ]
