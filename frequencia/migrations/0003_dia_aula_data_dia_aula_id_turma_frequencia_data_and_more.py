# Generated by Django 4.2.4 on 2023-09-19 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequencia', '0002_dia_aula_remove_frequencia_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dia_aula',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dia_aula',
            name='id_turma',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='id_aluno',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='id_turma',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='presenca',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
