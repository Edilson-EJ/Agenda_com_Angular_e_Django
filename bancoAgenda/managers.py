from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class UsuarioManager(BaseUserManager):

    #User Register
    def create_user(self, email_usuario, password, **extra_fields):
        if not email_usuario:
            raise ValueError(_('o email esta incorreto'))
        email = self.normalize_email(email_usuario)
        user = self.model(email_usuario=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # Super User Register
    
    def create_superuser(self,email_usuario,password, **extra_fields ):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_trusty', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Super mat have is+superuser=True.'))
        return self.create_user(email_usuario, password, **extra_fields)