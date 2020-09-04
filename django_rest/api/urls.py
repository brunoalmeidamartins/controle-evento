from django.urls import path, include
from .views import funcionario_view, convidado_view, evento_view, evento_funcionario_view

urlpatterns = [
    path('funcionarios/', funcionario_view.FuncionarioList.as_view(), name='funcionario-list'),
    path('funcionarios/<int:id>', funcionario_view.FuncionarioDetalhes.as_view(), name='funcionario-detalhes'),
    path('convidados/', convidado_view.ConvidadoList.as_view(), name='convidado-list'),
    path('convidados/<int:id>', convidado_view.ConvidadoDetalhes.as_view(), name='convidado-detalhes'),
    path('eventos/', evento_view.EventoList.as_view(), name='evento-list'),
    path('eventos/<int:id>', evento_view.EventoDetalhes.as_view(), name='evento-detalhes'),

    path('listar_evento/<int:id>', evento_funcionario_view.ListarEvento.as_view(), name='listar-evento'),
    path('participar_churrasco/', evento_funcionario_view.ParticiparChurrasco.as_view(), name='participar-churrasco'),
    path('cancelar_participacao/', evento_funcionario_view.CancelarParticipacao.as_view(), name='cancelar-participacao'),
    path('cancelar_participacao_convidado/', evento_funcionario_view.CancelarParticipacaoConvidado.as_view(), name='cancelar-participacao-convidado'),
    path('listar_participantes/<int:id>', evento_funcionario_view.ListarParticipantes.as_view(), name='listar-participantes'),
    path('listar_convidados/<int:id>', evento_funcionario_view.ListarConvidados.as_view(), name='listar-convidados'),
]
