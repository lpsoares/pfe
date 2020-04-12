#!/usr/bin/env python
"""
Desenvolvido para o Projeto Final de Engenharia
Autor: Luciano Pereira Soares <lpsoares@insper.edu.br>
Data: 18 de Outubro de 2019
"""

import datetime
from celery import task

from .messages import email
from .views import get_calendario_context
from .models import Configuracao, Aviso

@task
def envia_aviso():
    """Gera um aviso por e-mail."""
    configuracao = Configuracao.objects.all().first()
    delta = (datetime.date.today() - configuracao.t0).days
    avisos = Aviso.objects.filter(delta=delta)
    recipient_list = ['pfeinsper@gmail.com', 'lpsoares@insper.edu.br',]
    for aviso in avisos:
        subject = 'Aviso: '+aviso.titulo
        if aviso.mensagem:
            message = aviso.mensagem
        else:
            message = "Mensagem não definida."
        verify = email(subject, recipient_list, message)
        if verify != 1:
            #print("Algum problema de conexão, contacte: lpsoares@insper.edu.br")
            pass

    # Eventos do calendário
    context = get_calendario_context()
    for event in context:
        for acao in context[event]:
            if acao.startDate == datetime.date.today():
                subject = "{0} : {1}".format(event, acao.name)
                message = "Local : {0}".format(acao.location)
                message += "data inicial = {0}".format(acao.startDate)
                message += "data final = {0}".format(acao.endDate)
                message += "color = {0}".format(acao.color)
                verify = email(subject, recipient_list, message)
                if verify != 1:
                    #print("Algum problema de conexão, contacte: lpsoares@insper.edu.br")
                    pass
