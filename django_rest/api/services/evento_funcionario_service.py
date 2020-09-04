from ..services import funcionario_service, convidado_service
from ..models import Evento_Funcionario
from django.http import Http404
import json


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

def listar_participantes(eventos_funcionarios):
    obj_participantes = json.loads(json.dumps(eventos_funcionarios))
    vetor_ids_participantes = []
    for participante in obj_participantes:
        vetor_ids_participantes.append(participante["funcionario"])
    return funcionario_service.listar_funcionarios_ids(vetor_ids_participantes)

def listar_convidados(eventos_funcionarios):
    obj_convidados = json.loads(json.dumps(eventos_funcionarios))
    vetor_ids_convidados = []
    for convidado in obj_convidados:
        vetor_ids_convidados.append(convidado["convidado"])
    return convidado_service.listar_convidados_ids(vetor_ids_convidados)
    
    