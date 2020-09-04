from ..models import Evento_Funcionario
from django.http import Http404

def cadastrar_evento_funcionario(evento_funcionario):
    return Evento_Funcionario.objects.create(evento=evento_funcionario.evento,
                                            funcionario=evento_funcionario.funcionario, 
                                            convidado=evento_funcionario.convidado,
                                            funcionario_bebe=evento_funcionario.funcionario_bebe, 
                                            convidado_bebe=evento_funcionario.convidado_bebe)

def listar_evento_funcionarios_idEvento(id_evento):
    eventos_funcionarios = Evento_Funcionario.objects.filter(evento=id_evento)
    return eventos_funcionarios

def listar_evento_funcionario_idEvento_idFuncionario(id_evento, id_funcionario):
    try:
        return Evento_Funcionario.objects.get(evento=id_evento, funcionario=id_funcionario)
    except Evento_Funcionario.DoesNotExist:
        raise Http404

def remover_evento_funcionario(evento_funcionario):
    evento_funcionario.delete()

def cancelar_participacao_convidado(evento_funcionario):
    evento_funcionario.convidado = None
    evento_funcionario.save(force_update=True)
    return listar_evento_funcionario_idEvento_idFuncionario(evento_funcionario.evento, evento_funcionario.funcionario)