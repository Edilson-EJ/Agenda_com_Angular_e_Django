from django.shortcuts import render

from rest_framework import response,status, generics

from .models import BancoAgenda
from .serializers import BancoAgendaSerializer

#Método GET

class BancoAgendaList(generics.ListAPIView):

    queryset = BancoAgenda.objects.all()
    serializer_class = BancoAgendaSerializer

    def get( self, request):

        bancoAgenda_serializer = self.serializer_class(self.queryset.all(), many=True)

        return response.Response(data = bancoAgenda_serializer.data, status = status.HTTP_200_OK)



#Método POST

class BancoAgendaCreate(generics.CreateAPIView):

    queryset = BancoAgenda.objects.all()
    serializer_class = BancoAgendaSerializer

    def post(self, request):

        bancoAgenda_serializer = self.serializer_class(data = request.data)

        if bancoAgenda_serializer.is_valid():

            bancoAgenda_serializer.save()

            return response.Response(data = bancoAgenda_serializer.data, status = status.HTTP_201_CREATED)
        
        else:

            return response.Response(data = bancoAgenda_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# método PUT

class BancoAgendaUpdate(generics.RetrieveUpdateAPIView):

    queryset = BancoAgenda.objects.all()
    serializer_class = BancoAgendaSerializer

    def put(self, request,pk):

        bancoAgenda = self.queryset.get(pk = pk)

        bancoAgenda_serializer = self.serializer_class(bancoAgenda, request.data)

        if bancoAgenda_serializer.is_valid():

            bancoAgenda_serializer.save()

            return response.Response(data = bancoAgenda_serializer.data, status = status.HTTP_200_OK)

        else:

                return response.Response(data = bancoAgenda_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# método DELETE

class BancoAgendaDelete(generics.RetrieveDestroyAPIView):

    queryset = BancoAgenda.objects.all()
    serializer_class = BancoAgendaSerializer

    def delete(self, request, pk):

        bancoAgenda = self.queryset.get(pk = pk)

        bancoAgenda.delete()

        return response.Response(data = {}, status = status.HTTP_204_NO_CONTENT)

