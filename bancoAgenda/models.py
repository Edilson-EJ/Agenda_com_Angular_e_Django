from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UsuarioManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class BancoAgenda(AbstractBaseUser, PermissionsMixin):

    #Dados agendadamento 
    nome_agenda = models.CharField(_("Nome do agendamento"),max_length=100,unique=False)
    data = models.DateField(_("Data do agendamento"),null=True)
    email = models.CharField(_("Email do agendamento"),max_length=100)
    celular = models.CharField(_("Celular do agendamento"),max_length=100)
    assunto = models.CharField(_("Assunto do agendamento"),max_length=100)

    #Dados de acesso e permissão
    email_usuario = models.EmailField(_("Email do usuário"), max_length=255,unique=True)
    password = models.CharField(_("Senha do usuário"), max_length=255)
    is_staff = models.BooleanField(_("Administrador?"), default=False)
    is_active = models.BooleanField(_("Ativo"), default=True)
    is_trusty = models.BooleanField(_("Verificado"), default=True)
    date_joine = models.DateTimeField(_("Criação"), default=timezone.now)

    #Campo de autenticação
    USERNAME_FIELD = 'email_usuario'

    # Gerenciador de operações de criação
    objects = UsuarioManager()

    def __ste__(self):
        return self.nome_agenda

    class Meta:
        db_table = "bancoAgenda"
        app_label = "bancoAgenda"