from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import PFEUserCreationForm, PFEUserChangeForm
from .models import PFEUser, Aluno, Professor, Funcionario, Administrador, Opcao

@admin.register(PFEUser)
class PFEUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'tipo_de_usuario',) #na tabela com todos
    list_filter = ('tipo_de_usuario',)
    fieldsets = (
       (None, {'fields': ('username', 'first_name', 'last_name', 'email', 'tipo_de_usuario',)}),
        ('Personal info', {'fields': ('groups','user_permissions')}),
       ('Permissions', {'fields': ('is_active', 'is_staff','is_superuser',)}),
    )

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Funcionario)
admin.site.register(Administrador)

class OpcaoInline(admin.TabularInline):
    model = Opcao
    extra = 5
    max_num = 5

admin.site.register(Opcao)
