# Generated by Django 4.2.4 on 2023-09-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0003_alter_alunos_turma'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunos',
            name='numero',
            field=models.CharField(default='1', max_length=20),
            preserve_default=False,
        ),
    ]
