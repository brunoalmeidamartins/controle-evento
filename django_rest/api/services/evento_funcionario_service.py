from ..models import Evento_Funcionario
from django.http import Http404

def cadastrar_evento_funcionario(evento_funcionario):
    return Evento_Funcionario.objects.create(evento=evento_funcionario.evento,
                                            funcionario=evento_funcionario.funcionario, 
                                            convidado=evento_funcionario.convidado,
                                            funcionario_bebe=evento_funcionario.funcionario_bebe, 
                                            convidado_bebe=evento_funcionario.convidado_bebe)
