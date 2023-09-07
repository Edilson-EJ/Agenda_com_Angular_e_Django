from django.db import models
from django.utils.translation import gettext_lazy as _

class BancoAgenda(models.Model):
    nome_agenda = models.CharField(_("Nome do agendamento"),max_length=100)
    data = models.DateField(_("Data do agendamento"))
    email = models.CharField(_("Email do agendamento"),max_length=100)
    celular = models.CharField(_("Celular do agendamento"),max_length=100)
    assunto = models.CharField(_("Assunto do agendamento"),max_length=100)

    def __ste__(self):
        return self.nome_agenda

    class Meta:
        db_table = "bancoAgenda"
        app_label = "bancoAgenda"