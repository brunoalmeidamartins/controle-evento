from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..services import convidado_service
from ..serializers import convidado_serializer
from ..entidades import convidado


class ConvidadoList(APIView):
    def get(self, request, format=None):
        convidados = convidado_service.listar_convidados()
        serializer = convidado_serializer.ConvidadoSerializer(convidados, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = convidado_serializer.ConvidadoSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            funcionario = serializer.validated_data["funcionario"]
            convidado_novo = convidado.Convidado(nome=nome, funcionario=funcionario)
            convidado_service.cadastrar_convidado(convidado_novo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConvidadoDetalhes(APIView):
    def get(self, request, id, format=None):
        convidado = convidado_service.listar_convidado_id(id)
        serializer = convidado_serializer.ConvidadoSerializer(convidado)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, id, format=None):
        convidado_antigo = convidado_service.listar_convidado_id(id)
        serializer = convidado_serializer.ConvidadoSerializer(convidado_antigo, data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            funcionario = serializer.validated_data["funcionario"]
            convidado_novo = convidado.Convidado(nome=nome, funcionario=funcionario)
            convidado_service.editar_convidado(convidado_antigo, convidado_novo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        convidado = convidado_service.listar_convidado_id(id)
        convidado_service.remover_convidado(convidado)
        return Response(status=status.HTTP_204_NO_CONTENT)

