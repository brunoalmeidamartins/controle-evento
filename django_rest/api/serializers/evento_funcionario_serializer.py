from rest_framework import serializers
from ..models import Evento_Funcionario

class Evento_FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento_Funcionario
        fields = ('evento', 'funcionario', 'convidado', 'funcionario_bebe', 'convidado_bebe')
