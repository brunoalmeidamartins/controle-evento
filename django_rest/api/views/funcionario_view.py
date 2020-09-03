from rest_framework.views import APIView
from ..services import funcionario_service
from ..serializers import funcionario_serializer
from rest_framework.response import Response
from rest_framework import status
from ..entidades import funcionario

class FuncionarioList(APIView):
    def get(self, request, format=None):
        funcionarios = funcionario_service.listar_funcionarios()
        serializer = funcionario_serializer.FuncionarioSerializer(funcionarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    def post(self, request, format=None):
        serializer = funcionario_serializer.FuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            funcionario_novo = funcionario.Funcionario(nome=nome)
            funcionario_bd = funcionario_service.cadastrar_funcionario(funcionario_novo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class FuncionarioDetalhes(APIView):
    def get(self, request, id, format=None):
        funcionario = funcionario_service.listar_funcionario_id(id)
        serializer = funcionario_serializer.FuncionarioSerializer(funcionario)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, id, format=None):
        funcionario_antigo = funcionario_service.listar_funcionario_id(id)
        serializer = funcionario_serializer.FuncionarioSerializer(funcionario_antigo, data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            funcionario_novo = funcionario.Funcionario(nome=nome)
            funcionario_service.editar_funcionario(funcionario_antigo, funcionario_novo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        funcionario = funcionario_service.listar_funcionario_id(id)
        funcionario_service.remover_funcionario(funcionario)
        return Response(status=status.HTTP_204_NO_CONTENT)
