# Generated by Django 4.2.5 on 2023-10-31 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_agenda', models.CharField(max_length=100, verbose_name='Nome do agendamento')),
                ('data', models.DateField(null=True, verbose_name='Data do agendamento')),
                ('email', models.CharField(max_length=100, verbose_name='Email do agendamento')),
                ('celular', models.CharField(max_length=100, verbose_name='Celular do agendamento')),
                ('assunto', models.CharField(max_length=100, verbose_name='Assunto do agendamento')),
            ],
            options={
                'db_table': 'agendamento',
            },
        ),
    ]