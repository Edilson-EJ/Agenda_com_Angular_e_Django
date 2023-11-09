from rest_framework import serializers

from .models import BancoAgenda

#Importações do sistema
from .models import *

class UsuarioADMSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = UsuarioADM
        # campos que serão serializados, no caso, todos.
        fields = ["email_usuario","password"]
    
    # Criação do Usuário
    def create(self, validated_data):

        #criptografa a senha 
        return UsuarioADM.objects.create_user(**validated_data)
    
    #Atualização do Usuário
    def update(self, instance, validated_data):
        usuario = super().update(instance, validated_data)

        try:
            usuario.set_password(validated_data['password'])
            usuario.save()
        except KeyError:
            pass
        return usuario 