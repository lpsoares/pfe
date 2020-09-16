#!/usr/bin/env python
#pylint: disable=unused-argument
"""
Desenvolvido para o Projeto Final de Engenharia
Autor: Luciano Pereira Soares <lpsoares@insper.edu.br>
Data: 15 de Maio de 2019
"""

from functools import partial

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.utils.functional import curry

from projetos.models import Projeto, Proposta, Empresa, Organizacao, Avaliacao


####   PARA PORTAR AS AREAS DE INTERESSE DE ALUNOS PARA CÁ, E USAR NO PROJETO  #####
#areas de interesse
class Areas(models.Model):
    """Áreas de interesse dos projetos de engenharia."""
    inovacao_social = models.BooleanField("Inovacao Social",
                                          default=False)
    ciencia_dos_dados = models.BooleanField("Ciência dos Dados",
                                            default=False)
    modelagem_3D = models.BooleanField("Modelagem 3D",
                                       default=False)
    manufatura = models.BooleanField("Manufatura",
                                     default=False)
    resistencia_dos_materiais = models.BooleanField("Resistência dos Materiais",
                                                    default=False)
    modelagem_de_sistemas = models.BooleanField("Modelagem de Sistemas",
                                                default=False)
    controle_e_automacao = models.BooleanField("Controle e Automação",
                                               default=False)
    termodinamica = models.BooleanField("Termodinâmica",
                                        default=False)
    fluidodinamica = models.BooleanField("Fuidodinâmica",
                                         default=False)
    eletronica_digital = models.BooleanField("Eletrônica Digital",
                                             default=False)
    programacao = models.BooleanField("Programação",
                                      default=False)
    inteligencia_artificial = models.BooleanField("Inteligência Artificial",
                                                  default=False)
    computacao_em_nuvem = models.BooleanField("Computação em Nuvem",
                                              default=False)
    banco_de_dados = models.BooleanField("Banco de Dados",
                                         default=False)
    visao_computacional = models.BooleanField("Visão Computacional",
                                              default=False)
    computacao_de_alto_desempenho = models.BooleanField("Computação de Alto Desempenho",
                                                        default=False)
    robotica = models.BooleanField("Robótica",
                                   default=False)
    realidade_virtual_aumentada = models.BooleanField("Realidade Virtual e Aumentada",
                                                      default=False)
    protocolos_de_comunicacao = models.BooleanField("Protocolos de Comunicação",
                                                    default=False)
    eficiencia_energetica = models.BooleanField("Eficiência Energética",
                                                default=False)
    administracao_economia_financas = models.BooleanField("Administração/Economia/Finanças",
                                                          default=False)

    outras = models.CharField("Outras", max_length=128, null=True, blank=True,
                              help_text='Outras áreas de interesse')

    def __str__(self):
        return   ("V" if self.inovacao_social else "F") + " "\
               + ("V" if self.ciencia_dos_dados else "F") + " "\
               + ("V" if self.modelagem_3D else "F") + " "\
               + ("V" if self.manufatura else "F") + " "\
               + ("V" if self.resistencia_dos_materiais else "F") + " "\
               + ("V" if self.modelagem_de_sistemas else "F") + " "\
               + ("V" if self.controle_e_automacao else "F") + " "\
               + ("V" if self.termodinamica else "F") + " "\
               + ("V" if self.fluidodinamica else "F") + " "\
               + ("V" if self.eletronica_digital else "F") + " "\
               + ("V" if self.programacao else "F") + " "\
               + ("V" if self.inteligencia_artificial else "F") + " "\
               + ("V" if self.computacao_em_nuvem else "F") + " "\
               + ("V" if self.banco_de_dados else "F") + " "\
               + ("V" if self.visao_computacional else "F") + " "\
               + ("V" if self.computacao_de_alto_desempenho else "F") + " "\
               + ("V" if self.robotica else "F") + " "\
               + ("V" if self.realidade_virtual_aumentada else "F") + " "\
               + ("V" if self.protocolos_de_comunicacao else "F") + " "\
               + ("V" if self.eficiencia_energetica else "F") + " "\
               + ("V" if self.administracao_economia_financas else "F") + " "\
               + (self.outras[:32] if self.outras else "")

    class Meta:
        verbose_name = 'Áreas'
        verbose_name_plural = 'Áreas'

    @classmethod
    def create(cls):
        """Cria um objeto (entrada) em Areas."""
        areas = cls()
        return areas


class PFEUser(AbstractUser):
    """Classe base para todos os usuários do PFE (Alunos, Professores, Parceiros)."""
    # Atualizar para AbstractBaseUser que permite colocar mais caracteres nos campos
    #username
    #first_name
    #last_name
    #email
    #is_active
    # add additional fields in here
    TIPO_DE_USUARIO_CHOICES = (
        (1, 'aluno'),
        (2, 'professor'),
        (3, 'parceiro'),
        (4, 'administrador'),
    )
    tipo_de_usuario = models.PositiveSmallIntegerField(choices=TIPO_DE_USUARIO_CHOICES, default=1,
                                                       help_text='cada usuário tem um perfil único')
    cpf = models.CharField("CPF", max_length=11, null=True, blank=True,
                           help_text='CPF do usuário')
    linkedin = models.URLField("LinkedIn", max_length=250, null=True, blank=True,
                               help_text='LinkedIn do usuário')

    membro_comite = \
        models.BooleanField(default=False, help_text='caso membro do comitê do PFE')

    GENERO_CHOICES = (
        ('X', 'Nao Informado'),
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, default='X',
                              help_text='sexo do usuário')

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['first_name', 'last_name']

    @classmethod
    def create(cls):
        """Cria um objeto (entrada) em PFEUser."""
        user = cls()
        return user

    def __str__(self):
        return self.first_name + " " + self.last_name + \
            " (" + self.TIPO_DE_USUARIO_CHOICES[self.tipo_de_usuario-1][1] + ")"
        #return self.username #ver se atualizar isso para first_name não quebra o projeto

class Professor(models.Model):
    """Classe de usuários com estatus de Professor."""
    user = models.OneToOneField(PFEUser, related_name='professor', on_delete=models.CASCADE)

    TIPO_DEDICACAO = (
        ("TI", "Tempo Integral"),
        ("TP", 'Tempo Parcial'),
    )

    dedicacao = models.CharField("Dedicação", max_length=2,
                                 choices=TIPO_DEDICACAO, null=True, blank=True,
                                 help_text='Tipo de dedicação do professor')

    areas = models.TextField(max_length=500, blank=True)
    website = models.URLField(max_length=250, null=True, blank=True)
    lattes = models.URLField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ['user']
        permissions = (("altera_professor", "Professor altera valores"), )
    def __str__(self):
        return self.user.first_name+" "+self.user.last_name

    @classmethod
    def create(cls, usuario):
        """Cria um Professor e já associa o usuário."""
        professor = cls(user=usuario)
        return professor


## ISSO ESTA REPETIDO NO PROJETOS VIEWS / CUIDADO
def converte_conceito(conceito):
    """ Converte de Letra para Número. """
    if conceito == "A+":
        return 10
    elif conceito == "A" or conceito == "A ":
        return 9
    elif conceito == "B+":
        return 8
    elif conceito == "B" or conceito == "B ":
        return 7
    elif conceito == "C+":
        return 6
    elif conceito == "C" or conceito == "C ":
        return 5
    elif conceito == "D" or conceito == "D ":
        return 4
    return 0

def converte_letra(nota):
    """ Converte de Número para Letra. """
    if nota == 10:
        return "A+"
    elif nota >= 9:
        return "A"
    elif nota >= 8:
        return "B+"
    elif nota >= 7:
        return "B"
    elif nota >= 6:
        return "C+"
    elif nota >= 5:
        return "C"
    elif nota >= 4:
        return "D"
    return "I"

def get_notas(avalia):
    """ Faz a média de todas as notas de uma avaliação. """
    count = 0
    nota = 0
    if avalia.objetivo1:
        nota += converte_conceito(avalia.objetivo1_conceito)
        count += 1
    if avalia.objetivo2:
        nota += converte_conceito(avalia.objetivo2_conceito)
        count += 1
    if avalia.objetivo3:
        nota += converte_conceito(avalia.objetivo3_conceito)
        count += 1
    if avalia.objetivo4:
        nota += converte_conceito(avalia.objetivo4_conceito)
        count += 1
    if avalia.objetivo5:
        nota += converte_conceito(avalia.objetivo5_conceito)
        count += 1
    if count:
        return nota/count
    else:
        return 0



class Aluno(models.Model):
    """Classe de usuários com estatus de Aluno."""
    TIPOS_CURSO = (
        ('C', 'Computação'),
        ('M', 'Mecânica'),
        ('X', 'Mecatrônica'),
    )
    user = models.OneToOneField(PFEUser, related_name='aluno', on_delete=models.CASCADE)
    matricula = models.CharField("Matrícula", max_length=8, null=True, blank=True,
                                 help_text='Número de matrícula')
    #bio = models.TextField(max_length=500, blank=True)
    curso = models.CharField(max_length=1, choices=TIPOS_CURSO,
                             help_text='Curso Matriculado',)
    opcoes = models.ManyToManyField(Proposta, through='Opcao',
                                    help_text='Opcoes de projeto escolhidos')
    nascimento = models.DateField(null=True, blank=True,
                                  help_text='Data de nascimento')
    local_de_origem = models.CharField(max_length=30, blank=True,
                                       help_text='Local de nascimento')
    email_pessoal = models.EmailField(null=True, blank=True,
                                      help_text='e-mail pessoal')

    anoPFE = models.PositiveIntegerField(null=True, blank=True,
                                         validators=[MinValueValidator(2018),
                                                     MaxValueValidator(3018)],
                                         help_text='Ano que cursará o PFE')
    semestrePFE = models.PositiveIntegerField(null=True, blank=True,
                                              validators=[MinValueValidator(1),
                                                          MaxValueValidator(2)],
                                              help_text='Semestre que cursará o PFE')
    trancado = models.BooleanField(default=False,
                                   help_text='Caso o aluno tenha trancado ou abandonado o curso')
    cr = models.FloatField(default=0,
                           help_text='Coeficiente de Rendimento')

    pre_alocacao = models.ForeignKey(Proposta, null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name='aluno_pre_alocado',
                                     help_text='proposta pre alocada')

    areas_de_interesse = models.ForeignKey(Areas, on_delete=models.SET_NULL,
                                           null=True, blank=True,
                                           help_text='Áreas de interesse dos alunos')

    trabalhou = models.TextField(max_length=1000, null=True, blank=True,
                                 help_text='Trabalhou ou estagio em alguma empresa de engenharia?')
    social = models.TextField(max_length=1000, null=True, blank=True,
                              help_text='Já participou de atividade sociais?')
    entidade = models.TextField(max_length=1000, null=True, blank=True,
                                help_text='Já participou de alguma entidade estudantil do Insper?')
    familia = models.TextField(max_length=1000, null=True, blank=True,\
              help_text='Possui familiares em empresa que está aplicando? Ou empresa concorrente?')

    #https://bradmontgomery.net/blog/django-hack-help-text-modal-instance/
    def _get_help_text(self, field_name):
        """Given a field name, return it's help text."""
        for field in self._meta.fields:
            if field.name == field_name:
                return field.help_text

    def __init__(self, *args, **kwargs):
        # Call the superclass first; it'll create all of the field objects.
        super(Aluno, self).__init__(*args, **kwargs)

        # Again, iterate over all of our field objects.
        for field in self._meta.fields:
            # Create a string, get_FIELDNAME_help text
            method_name = "get_{0}_help_text".format(field.name)

            # We can use curry to create the method with a pre-defined argument
            curried_method = partial(self._get_help_text, field_name=field.name)

            # And we add this method to the instance of the class.
            setattr(self, method_name, curried_method)

    def get_curso(self):
        """Retorna em string o nome do curso."""
        for entry in Aluno.TIPOS_CURSO:
            if self.curso == entry[0]:
                return entry[1]
        return "Sem evento"

    @property
    def get_banca_i(self):
        """Retorna média."""
        alocacoes = Alocacao.objects.filter(aluno=self.pk)
        if alocacoes:

            #supondo só uma alocação para agora
            alocacao = alocacoes.first()

            nota_banca_intermediaria = 0

            avaliacoes_banca_intermediaria = Avaliacao.objects.filter(projeto=alocacao.projeto,
                                                                    tipo_de_entrega=0, # Banca
                                                                    tipo_de_banca=1) #(1, 'intermediária')

            for avali in avaliacoes_banca_intermediaria:
                nota_banca_intermediaria += get_notas(avali)
            if avaliacoes_banca_intermediaria:
                media = nota_banca_intermediaria/len(avaliacoes_banca_intermediaria)
                return media
            else:
                return -1000

        return -1000

    @property
    def get_banca_f(self):
        """Retorna média."""
        alocacoes = Alocacao.objects.filter(aluno=self.pk)
        if alocacoes:

            #supondo só uma alocação para agora
            alocacao = alocacoes.first()

            nota_banca_final = 0
            
            avaliacoes_banca_final = Avaliacao.objects.filter(projeto=alocacao.projeto,
                                                                    tipo_de_entrega=0, # Banca
                                                                    tipo_de_banca=0) #(0, 'final')
            for avali in avaliacoes_banca_final:
                nota_banca_final += get_notas(avali)
            if avaliacoes_banca_final:
                media = nota_banca_final/len(avaliacoes_banca_final)
                return media
            else:
                return -1000
        return -1000

    @property
    def get_notas(self):
        return [("BI", self.get_banca_i, 0.1),("BF", self.get_banca_f, 0.1)]
    
    @property
    def get_media(self):
        """Retorna média."""
        nota_final = 0
        for aval, nota, peso in self.get_notas:
            nota_final += nota * peso
        return nota_final

    class Meta:
        ordering = ['user']
        permissions = ()
    def __str__(self):
        return self.user.get_full_name()

    @classmethod
    def create(cls, usuario):
        """Cria um Estudante e já associa o usuário."""
        estudante = cls(user=usuario)
        return estudante

class Opcao(models.Model):
    """Opções de Projetos pelos Alunos com suas prioridades."""
    proposta = models.ForeignKey(Proposta, null=True, blank=True, on_delete=models.SET_NULL)
    aluno = models.ForeignKey(Aluno, null=True, blank=True, on_delete=models.CASCADE)
    #razao = models.CharField(max_length=200)
    prioridade = models.PositiveSmallIntegerField()
    class Meta:
        verbose_name = 'Opção'
        verbose_name_plural = 'Opções'
        ordering = ['prioridade']
        permissions = (("altera_professor", "Professor altera valores"), )
    def __str__(self):
        return self.aluno.user.username + " >>> " + self.proposta.titulo

class Alocacao(models.Model):
    """Projeto em que o aluno está alocado."""
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    
    # OBSOLETO NÃO DEVE SER USADO E DEVE SER REMOVIDO !!!!!
    CONCEITOS = (
        (127, 'NA'),
        (10, 'A+'),
        (9, 'A'),
        (8, 'B+'),
        (7, 'B'),
        (6, 'C+'),
        (5, 'C'),
        (4, 'D'),
        (0, 'I'),
    )
    conceito = models.PositiveSmallIntegerField(choices=CONCEITOS, default=127)
    #############################################################################


    class Meta:
        verbose_name = 'Alocação'
        verbose_name_plural = 'Alocações'
        permissions = (("altera_professor", "Professor altera valores"), )
        ordering = ['projeto__ano', 'projeto__semestre',]
    def __str__(self):
        return self.aluno.user.username+" >>> "+self.projeto.titulo

    @classmethod
    def create(cls, estudante, projeto):
        """Cria um Projeto (entrada) de Alocação."""
        alocacao = cls(projeto=projeto, aluno=estudante)
        return alocacao

class Parceiro(models.Model):  # da empresa (não do Insper)
    """Classe de usuários com estatus de Parceiro (pessoal das organizações parceiras)."""
    user = models.OneToOneField(PFEUser, related_name='parceiro', on_delete=models.CASCADE,
                                help_text='Identificaçãdo do usuário')
    organizacao_old = models.ForeignKey(Empresa, on_delete=models.CASCADE,
                                        blank=True, null=True,
                                        help_text='Não mais utilizado')

    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE,
                                    blank=True, null=True,
                                    help_text='Organização Parceira')

    cargo = models.CharField("Cargo", max_length=90, blank=True,
                             help_text='Cargo Funcional')
    telefone = models.CharField(max_length=20, blank=True,
                                help_text='Telefone Fixo')
    celular = models.CharField(max_length=20, blank=True,
                               help_text='Telefone Celular')
    skype = models.CharField(max_length=32, blank=True,
                             help_text='Identificação Skype')
    observacao = models.TextField("Observações", max_length=500, blank=True,
                                  help_text='Observações')

    principal_contato = models.BooleanField("Principal Contato", default=False)

    class Meta:
        ordering = ['user']
        permissions = (("altera_parceiro", "Parceiro altera valores"),)

    def __str__(self):
        if self.organizacao:
            return self.user.get_full_name()+" ["+self.organizacao.sigla+"]"
        else:
            return self.user.get_full_name()
    
    @classmethod
    def create(cls, usuario):
        """Cria um Parceiro e já associa o usuário."""
        parceiro = cls(user=usuario)
        return parceiro

class Administrador(models.Model):
    """Classe de usuários com estatus de Administrador."""
    user = models.OneToOneField(PFEUser, related_name='administrador', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
        ordering = ['user']
        permissions = (("altera_empresa", "Empresa altera valores"),
                       ("altera_professor", "Professor altera valores"), )
    def __str__(self):
        return self.user.username
    
    # @classmethod
    # def create(cls, usuario):
    #     """Cria um Administrador e já associa o usuário."""
    #     administrador = cls(user=usuario)
    #     return administrador


# REMOVER ISSO, ESTÁ DANDO PROBLEMA
# VER FINAL DE : https://stackoverflow.com/questions/24063057/django-duplicate-key-error-but-key-does-not-exist/24222067#24222067

# @receiver(post_save, sender=PFEUser)
# def create_user_dependency(sender, instance, created, **kwargs):
#     """Quando um usuário do PFE é criado/salvo, seu corespondente específico também é criado."""
#     #print("Chamado -------------------")
#     if instance.tipo_de_usuario == 1: #aluno
#         Aluno.objects.get_or_create(user=instance)
#     elif instance.tipo_de_usuario == 2: #professor
#         Professor.objects.get_or_create(user=instance)
#     elif instance.tipo_de_usuario == 3: #Parceiro
#         Parceiro.objects.get_or_create(user=instance)
#     elif instance.tipo_de_usuario == 4: #administrador
#         Administrador.objects.get_or_create(user=instance)

# @receiver(post_save, sender=PFEUser)
# def save_user_dependency(sender, instance, **kwargs):
#     """Quando um usuário do PFE é criado/salvo, seu corespondente específico também é criado."""
#     if instance.tipo_de_usuario == 1: #aluno
#         instance.aluno.save()
#     elif instance.tipo_de_usuario == 2: #professor
#         instance.professor.save()
#     elif instance.tipo_de_usuario == 3: #Parceiro
#         instance.parceiro.save()
#     elif instance.tipo_de_usuario == 4: #administrador
#         instance.administrador.save()
