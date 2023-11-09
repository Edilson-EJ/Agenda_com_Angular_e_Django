from django.urls import path

from .views import *

urlpatterns = [
    path("",AgendamentoList.as_view(), name="agendamento-list"),
    path("create/", AgendamentoCreate.as_view(), name="agendamento-create"),
    path("update/<int:pk>/", AgendamentoUpdate.as_view(), name="agendamento-update"),
    path("delete/<int:pk>/", AgendamentoDelete.as_view(), name="agentamento-delete")
]