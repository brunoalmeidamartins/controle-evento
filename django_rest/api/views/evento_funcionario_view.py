from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..services import evento_funcionario_service
from ..serializers import evento_funcionario_serializer
from ..entidades import evento_funcionario

class ParticiparChurrasco(APIView):
    def post(self, request, format=None):
        serializer = evento_funcionario_serializer.Evento_FuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            evento = serializer.validated_data["evento"]
            funcionario = serializer.validated_data["funcionario"]
            convidado = serializer.validated_data["convidado"]
            funcionario_bebe = serializer.validated_data["funcionario_bebe"]
            convidado_bebe = serializer.validated_data["convidado_bebe"]
            evento_funcionario_novo = evento_funcionario.EventoFuncionario(evento=evento, 
                                                                            funcionario=funcionario,
                                                                            convidado=convidado,
                                                                            funcionario_bebe=funcionario_bebe,
                                                                            convidado_bebe=convidado_bebe)
            evento_funcionario_service.cadastrar_evento_funcionario(evento_funcionario_novo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)