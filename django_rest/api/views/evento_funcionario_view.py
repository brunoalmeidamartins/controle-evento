from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..services import evento_funcionario_service
from ..serializers import evento_funcionario_serializer, funcionario_serializer
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

class ListarEvento(APIView):
    def get(self, request, id, format=None):
        eventos_funcionarios = evento_funcionario_service.listar_evento_funcionarios_idEvento(id)
        serializer = evento_funcionario_serializer.Evento_FuncionarioSerializer(eventos_funcionarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CancelarParticipacao(APIView):
    def delete(self, request, format=None):
        serializer = evento_funcionario_serializer.CancelarParticipacaoSerializer(data=request.data)
        if serializer.is_valid():
            evento = serializer.validated_data["evento"]
            funcionario = serializer.validated_data["funcionario"]
            evento_funcionario_bd = evento_funcionario_service.listar_evento_funcionario_idEvento_idFuncionario(evento, funcionario)
            evento_funcionario_service.remover_evento_funcionario(evento_funcionario_bd)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class CancelarParticipacaoConvidado(APIView):
    def put(self, request, format=None):
        serializer = evento_funcionario_serializer.CancelarParticipacaoConvidadoSerializer(data=request.data)
        if serializer.is_valid():
            evento = serializer.validated_data["evento"]
            funcionario = serializer.validated_data["funcionario"]
            evento_funcionario_bd = evento_funcionario_service.listar_evento_funcionario_idEvento_idFuncionario(evento, funcionario)
            obj_ef = evento_funcionario_service.cancelar_participacao_convidado(evento_funcionario_bd)
            serializer_ef = evento_funcionario_serializer.Evento_FuncionarioSerializer(obj_ef)
            return Response(serializer_ef.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListarParticipantes(APIView):
    def get(self, request, id, format=None):
        eventos_funcionarios = evento_funcionario_service.listar_evento_funcionarios_idEvento(id)
        serializer = evento_funcionario_serializer.ListarParticipantesSerializer(eventos_funcionarios, many=True)
        participantes = evento_funcionario_service.listar_participantes(serializer.data)
        serializer_participantes = funcionario_serializer.FuncionarioSerializer(participantes, many=True)
        return Response(serializer_participantes.data, status=status.HTTP_200_OK)

class ListarConvidados(APIView):
    def get(self, request, id, format=None):
        eventos_funcionarios = evento_funcionario_service.listar_evento_funcionarios_idEvento(id)
        serializer = evento_funcionario_serializer.ListarConvidadosSerializer(eventos_funcionarios, many=True)
        convidados = evento_funcionario_service.listar_convidados(serializer.data)
        serializer_convidados = funcionario_serializer.FuncionarioSerializer(convidados, many=True)
        return Response(serializer_convidados.data, status=status.HTTP_200_OK)