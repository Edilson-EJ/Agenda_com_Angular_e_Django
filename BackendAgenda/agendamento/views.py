from rest_framework import response, status, generics

from .models import Agendamento
from .serializers import AgendamentoSerializer
from rest_framework.permissions import IsAuthenticated

# MÉTODO GET

class AgendamentoList(generics.ListAPIView):

    permission_classes = (IsAuthenticated, )

    # Definindo o queryset do método
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

    # Sobrescrevendo o queryset do método
    def get(self, resquest):

        agendamento_serializer = self.serializer_class(self.queryset.all(), many=True)

        return response.Response(data = agendamento_serializer.data, status = status.HTTP_200_OK)

# MÉTODO POST

class AgendamentoCreate(generics.CreateAPIView):

    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

    def post(self,request):
        
        agendamento_serializer = self.serializer_class(data = request.data)

        if agendamento_serializer.is_valid():
            agendamento_serializer.save()

            return response.Response(data = agendamento_serializer.data, status= status.HTTP_201_CREATED)
        
        else:

            return response.Response(data = agendamento_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

# método PUT

class AgendamentoUpdate(generics.RetrieveUpdateAPIView):

    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

    def put(self, request,pk):

        agendamento = self.queryset.get(pk = pk)

        agendamento_serializer = self.serializer_class(agendamento, request.data)

        if agendamento_serializer.is_valid():

            agendamento_serializer.save()

            return response.Response(data = agendamento_serializer.data, status = status.HTTP_200_OK)

        else:

                return response.Response(data = agendamento_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# método DELETE

class AgendamentoDelete(generics.RetrieveDestroyAPIView):

    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

    def delete(self, request, pk):

        agendamento = self.queryset.get(pk = pk)

        agendamento.delete()

        return response.Response(data = {}, status = status.HTTP_204_NO_CONTENT)

