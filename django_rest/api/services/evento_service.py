from ..models import Evento
from django.http import Http404

def listar_eventos():
    eventos = Evento.objects.all()
    return eventos

def cadastrar_evento(evento):
    return Evento.objects.create(nome=evento.nome, total_arrecadado=evento.total_arrecadado,
                                 total_gasto=evento.total_gasto, 
                                 total_gasto_comida=evento.total_gasto_comida,
                                 total_gasto_bebida=evento.total_gasto_bebida)

def listar_evento_id(id):
    try:
        return Evento.objects.get(id=id)
    except Evento.DoesNotExist:
        raise Http404

def editar_evento(evento_antigo, evento_novo):
    evento_antigo.nome = evento_novo.nome
    evento_antigo.save(force_update=True)

def remover_evento(evento):
    evento.delete()