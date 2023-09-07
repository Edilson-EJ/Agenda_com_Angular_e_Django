from django.urls import path

from .views import *

urlpatterns =[
    path("", BancoAgendaList.as_view(), name="bancoAgenda-list"),
    path("create/", BancoAgendaCreate.as_view(), name="bancoAgenda-create"),
    path("update/<int:pk>/",BancoAgendaUpdate.as_view(), name="bancoAgenda-update"),
    path("delete/<int:pk>/",BancoAgendaDelete.as_view(), name="bancoAgenda-delete")

]