from ..models import Convidado
from django.http import Http404

def listar_convidados():
    convidados = Convidado.objects.all()
    return convidados

def cadastrar_convidado(convidado):
    return Convidado.objects.create(nome=convidado.nome, 
                                            funcionario=convidado.funcionario)

def listar_convidado_id(id):
    try:
        return Convidado.objects.get(id=id)
    except Convidado.DoesNotExist:
        raise Http404

def editar_convidado(convidado_antigo, convidado_novo):
    convidado_antigo.nome = convidado_novo.nome
    convidado_antigo.save(force_update=True)

def remover_convidado(convidado):
    convidado.delete()