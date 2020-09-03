from ..models import Funcionario
from django.http import Http404

def listar_funcionarios():
    funcionarios = Funcionario.objects.all()
    return funcionarios

def cadastrar_funcionario(funcionario):
    return Funcionario.objects.create(nome=funcionario.nome)

def listar_funcionario_id(id):
    try:
        return Funcionario.objects.get(id=id)
    except Funcionario.DoesNotExist:
        raise Http404

def editar_funcionario(funcionario_antigo, funcionario_novo):
    funcionario_antigo.nome = funcionario_novo.nome
    funcionario_antigo.save(force_update=True)

def remover_funcionario(funcionario):
    funcionario.delete()