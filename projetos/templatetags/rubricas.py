#!/usr/bin/env python
"""
Desenvolvido para o Projeto Final de Engenharia
Autor: Luciano Pereira Soares <lpsoares@insper.edu.br>
Data: 22 de Abril de 2020
"""

from django import template
register = template.Library()

@register.filter
def get_rubrica(objetivos, objetivo):
    """Permite buscar uma rubrica."""
    return objetivos.get(id=objetivo)

@register.filter
def get_texto_conceito(objetivo, conceito):
    """Permite buscar o texto de uma rubrica."""
    if conceito == "A " or conceito == "A+":
        return objetivo.rubrica_A
    if conceito == "B " or conceito == "B+":
        return objetivo.rubrica_B
    if conceito == "C " or conceito == "C+":
        return objetivo.rubrica_C
    if conceito == "D ":
        return objetivo.rubrica_D
    if conceito == "I ":
        return objetivo.rubrica_I
    return "Erro"

@register.filter
def get_texto_nota(objetivo, nota):
    """Permite buscar o texto de uma rubrica."""
    if nota >= 9:
        return objetivo.rubrica_A
    if nota >= 7:
        return objetivo.rubrica_B
    if nota >= 5:
        return objetivo.rubrica_C
    if nota >= 4:
        return objetivo.rubrica_D
    if nota >= 0:
        return objetivo.rubrica_I
    return "Erro"