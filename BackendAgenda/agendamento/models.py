from django.db import models
from django.utils.translation import gettext_lazy as _

class Agendamento(models.Model):

    #Dados agendadamento 
    nome_agenda = models.CharField(_("Nome do agendamento"),max_length=100,unique=False)
    data = models.DateField(_("Data do agendamento"),null=True)
    email = models.CharField(_("Email do agendamento"),max_length=100)
    celular = models.CharField(_("Celular do agendamento"),max_length=100)
    assunto = models.CharField(_("Assunto do agendamento"),max_length=100)

    def __str__(self):
        return self.nome_agenda
    
    class Meta:
        db_table = "agendamento"
        app_label = "agendamento"
