from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..services import evento_service
from ..serializers import evento_serializer
from ..entidades import evento


class EventoList(APIView):
    def get(self, request, format=None):
        eventos = evento_service.listar_eventos()
        serializer = evento_serializer.EventoSerializer(eventos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = evento_serializer.EventoSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            total_arrecadado = serializer.validated_data["total_arrecadado"]
            total_gasto = serializer.validated_data["total_gasto"]
            total_gasto_comida = serializer.validated_data["total_gasto_comida"]
            total_gasto_bebida = serializer.validated_data["total_gasto_bebida"]
            evento_novo = evento.Evento(nome=nome, total_arrecadado=total_arrecadado,
            total_gasto=total_gasto, total_gasto_comida=total_gasto_comida,
            total_gasto_bebida=total_gasto_bebida)
            evento_service.cadastrar_evento(evento_novo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventoDetalhes(APIView):
    def get(self, request, id, format=None):
        evento = evento_service.listar_evento_id(id)
        serializer = evento_serializer.EventoSerializer(evento)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, id, format=None):
        evento_antigo = evento_service.listar_evento_id(id)
        serializer = evento_serializer.EventoSerializer(evento_antigo, data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            total_arrecadado = serializer.validated_data["total_arrecadado"]
            total_gasto = serializer.validated_data["total_gasto"]
            total_gasto_comida = serializer.validated_data["total_gasto_comida"]
            total_gasto_bebida = serializer.validated_data["total_gasto_bebida"]
            evento_novo = evento.Evento(nome=nome, total_arrecadado=total_arrecadado,
            total_gasto=total_gasto, total_gasto_comida=total_gasto_comida,
            total_gasto_bebida=total_gasto_bebida)
            evento_service.editar_evento(evento_antigo, evento_novo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        evento = evento_service.listar_evento_id(id)
        evento_service.remover_evento(evento)
        return Response(status=status.HTTP_204_NO_CONTENT)

class TotalGasto(APIView):
    def get(self, request, id, format=None):
        evento = evento_service.listar_evento_id(id)
        serializer = evento_serializer.TotalGasto(evento)
        return Response(serializer.data, status.HTTP_200_OK)

class TotalGastoComida(APIView):
    def get(self, request, id, format=None):
        evento = evento_service.listar_evento_id(id)
        serializer = evento_serializer.TotalGastoComida(evento)
        return Response(serializer.data, status.HTTP_200_OK)

class TotalGastoBebida(APIView):
    def get(self, request, id, format=None):
        evento = evento_service.listar_evento_id(id)
        serializer = evento_serializer.TotalGastoBebida(evento)
        return Response(serializer.data, status.HTTP_200_OK)