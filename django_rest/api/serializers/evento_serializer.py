from rest_framework import serializers
from ..models import Evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('nome', 'total_arrecadado', 'total_gasto', 'total_gasto_comida', 'total_gasto_bebida')

class TotalGastoComida(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('total_gasto_comida',)