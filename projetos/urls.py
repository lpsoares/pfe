#!/usr/bin/env python
# pylint: disable=C0103
"""
Desenvolvido para o Projeto Final de Engenharia
Autor: Luciano Pereira Soares <lpsoares@insper.edu.br>
Data: 15 de Maio de 2019
"""

from django.urls import path

from . import views

from organizacoes.views import projeto_feedback

urlpatterns = [
    path('', views.index, name='index'), #pagina inicial
    path('index_projetos/', views.index_projetos, name='index_projetos'), #pagina inicial de projs.

    path('carrega_bancos/', views.carrega_bancos, name='carrega_bancos'),
    path('comite/', views.comite, name='comite'),
    path('completo/<int:primakey>', views.projeto_completo, name='completo'), # REMOVER
    path('dinamicas/<str:periodo>', views.dinamicas, name='dinamicas'),
    path('dinamicas/', views.dinamicas_root, name='dinamicas_root'),
    path('distribuicao_areas/', views.distribuicao_areas, name='distribuicao_areas'),
    
    path('graficos/', views.graficos, name='graficos'),
    path('lista_feedback', views.lista_feedback, name='lista_feedback'),
    path('meuprojeto/', views.meuprojeto, name='meuprojeto'),
    path('migracao/', views.migracao, name='migracao'),
    path('mostra_feedback/<int:feedback_id>', views.mostra_feedback, name='mostra_feedback'),

    path('nomes/', views.nomes, name='nomes'),

    path('projeto_completo/<int:primakey>', views.projeto_completo, name='projeto_completo'),
    path('projeto_detalhes/<int:primarykey>', views.projeto_detalhes, name='projeto_detalhes'),

    # Antigo, remover depois
    path('projeto_feedback', projeto_feedback, name='projeto_feedback_old'),

    path('projetos_fechados/', views.projetos_fechados, name='projetos_fechados'),
    path('projetos_lista/<str:periodo>', views.projetos_lista, name='projetos_lista'),
    path('reembolso_pedir/', views.reembolso_pedir, name='reembolso_pedir'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('ajax/validate_aviso/', views.validate_aviso, name='validate_aviso'),

]
