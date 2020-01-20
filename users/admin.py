#!/usr/bin/env python
"""
Desenvolvido para o Projeto Final de Engenharia
Autor: Luciano Pereira Soares <lpsoares@insper.edu.br>
Data: 15 de Maio de 2019
"""

from django.contrib import admin
#from django.contrib.auth import get_user_model
#from django.contrib.auth.admin import UserAdmin

#from .forms import PFEUserCreationForm
#from .forms import PFEUserChangeForm
from .models import PFEUser, Aluno, Professor, Parceiro, Administrador

from .models import Opcao, Alocacao, Areas   # Mover para outra área

@admin.register(PFEUser)
class PFEUserAdmin(admin.ModelAdmin):
    """Usuário geral para todos do PFE."""
    list_display = ('first_name', 'last_name', 'username', 'email', 'tipo_de_usuario',)
    list_filter = ('tipo_de_usuario',)
    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'email', 'tipo_de_usuario',)}),
        ('Personal info', {'fields': ('groups', 'user_permissions', 'cpf', 'membro_comite')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )
    ordering = ('first_name', 'last_name')

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    """Definição de aluno do PFE."""
    list_display = ('user', 'curso', 'anoPFE', 'semestrePFE')
    ordering = ('user__first_name', 'user__last_name',)

@admin.register(Alocacao)
class AlocacaoAdmin(admin.ModelAdmin):
    """Definição de Alocacao do PFE."""
    list_display = ('aluno', 'projeto',)
    ordering = ('-projeto__ano', '-projeto__semestre',)

@admin.register(Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
    """Definição de Parceiro do PFE."""
    list_display = ('get_full_name', 'email', 'telefone', 'celular', 'skype')
    ordering = ()

    def get_full_name(self, obj):
        """Retorna o nome completo do usuário"""
        return obj.user.first_name+" "+obj.user.last_name
    get_full_name.short_description = 'Nome Completo'
    get_full_name.admin_order_field = 'user__first_name'

    def email(self, obj):
        """Retorna o e-mail do usuário"""
        return obj.user.email
    get_full_name.short_description = 'e-mail'

admin.site.register(Professor)
admin.site.register(Administrador)
admin.site.register(Opcao)
admin.site.register(Areas)

class OpcaoInline(admin.TabularInline):
    """.Não me lembro onde uso isso, provavel código morto."""
    model = Opcao
    extra = 5
    max_num = 5
