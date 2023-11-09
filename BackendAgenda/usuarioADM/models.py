from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UsuarioManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class UsuarioADM(AbstractBaseUser, PermissionsMixin):

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
