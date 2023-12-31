# Generated by Django 4.2.5 on 2023-10-19 13:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('bancoAgenda', '0004_alter_bancoagenda_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='bancoagenda',
            name='date_joine',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criação'),
        ),
        migrations.AddField(
            model_name='bancoagenda',
            name='email_usuario',
            field=models.EmailField(default=True, max_length=255, unique=True, verbose_name='Email do usuário'),
        ),
        migrations.AddField(
            model_name='bancoagenda',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='bancoagenda',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AddField(
            model_name='bancoagenda',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Administrador?'),
        ),
        migrations.AddField(
            model_name='bancoagenda',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='bancoagenda',
            name='is_trusty',
            field=models.BooleanField(default=True, verbose_name='Verificado'),
        ),
        migrations.AddField(
            model_name='bancoagenda',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='bancoagenda',
            name='password',
            field=models.CharField(default=True, max_length=255, unique=True, verbose_name='Senha do usuário'),
        ),
        migrations.AddField(
            model_name='bancoagenda',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='bancoagenda',
            name='assunto',
            field=models.CharField(max_length=100, unique=True, verbose_name='Assunto do agendamento'),
        ),
        migrations.AlterField(
            model_name='bancoagenda',
            name='celular',
            field=models.CharField(max_length=100, unique=True, verbose_name='Celular do agendamento'),
        ),
        migrations.AlterField(
            model_name='bancoagenda',
            name='data',
            field=models.DateField(unique=True, verbose_name='Data do agendamento'),
        ),
        migrations.AlterField(
            model_name='bancoagenda',
            name='email',
            field=models.CharField(max_length=100, unique=True, verbose_name='Email do agendamento'),
        ),
        migrations.AlterField(
            model_name='bancoagenda',
            name='nome_agenda',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nome do agendamento'),
        ),
    ]
