from django.urls import path, include
from .views import funcionario_view, convidado_view, evento_view, evento_funcionario_view

urlpatterns = [
    path('funcionarios/', funcionario_view.FuncionarioList.as_view(), name='funcionario-list'),
    path('funcionarios/<int:id>', funcionario_view.FuncionarioDetalhes.as_view(), name='funcionario-detalhes'),
    path('convidados/', convidado_view.ConvidadoList.as_view(), name='convidado-list'),
    path('convidados/<int:id>', convidado_view.ConvidadoDetalhes.as_view(), name='convidado-detalhes'),
    path('eventos/', evento_view.EventoList.as_view(), name='evento-list'),
    path('eventos/<int:id>', evento_view.EventoDetalhes.as_view(), name='evento-detalhes'),

    path('participar_churrasco/', evento_funcionario_view.ParticiparChurrasco.as_view(), name='participar-churrasco'),
]
