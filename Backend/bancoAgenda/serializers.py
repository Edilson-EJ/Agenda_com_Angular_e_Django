from rest_framework import serializers

from .models import BancoAgenda

class BancoAgendaSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = BancoAgenda

        fields = "__all__"