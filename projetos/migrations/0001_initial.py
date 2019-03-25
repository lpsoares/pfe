# Generated by Django 2.1.7 on 2019-03-25 02:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('login', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nome_completo', models.CharField(help_text='Nome completo do aluno', max_length=80)),
                ('curso', models.CharField(choices=[('C', 'Computacao'), ('M', 'Mecanica'), ('X', 'Mecatronica')], help_text='Curso Matriculado', max_length=1)),
                ('nascimento', models.DateField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_pessoal', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'ordering': ['nome_completo'],
                'permissions': (('altera_professor', 'Professor altera valores'),),
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('login', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nome_empresa', models.CharField(max_length=80)),
                ('sigla', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['sigla'],
                'permissions': (('altera_empresa', 'Empresa altera valores'), ('altera_professor', 'Professor altera valores')),
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('login', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=80)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetos.Empresa')),
            ],
            options={
                'ordering': ['nome'],
                'permissions': (('altera_empresa', 'Empresa altera valores'), ('altera_professor', 'Professor altera valores')),
            },
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao', models.CharField(max_length=200)),
                ('prioridade', models.PositiveSmallIntegerField(default=0)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetos.Aluno')),
            ],
            options={
                'ordering': ['prioridade'],
                'permissions': (('altera_professor', 'Professor altera valores'),),
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('login', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=80)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'ordering': ['nome'],
                'permissions': (('altera_professor', 'Professor altera valores'),),
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Titulo do projeto', max_length=100)),
                ('abreviacao', models.CharField(help_text='Abreviacao usada para o projeto', max_length=10)),
                ('descricao', models.TextField(help_text='Descricao do projeto', max_length=1000)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='')),
                ('ano', models.PositiveIntegerField(help_text='Ano que o projeto comeca', validators=[django.core.validators.MinValueValidator(2018), django.core.validators.MaxValueValidator(3018)])),
                ('semestre', models.PositiveIntegerField(help_text='Semestre que o projeto comeca', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)])),
                ('disponivel', models.BooleanField(default=False)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetos.Empresa')),
            ],
            options={
                'ordering': ['abreviacao'],
                'permissions': (('altera_empresa', 'Empresa altera valores'), ('altera_professor', 'Professor altera valores')),
            },
        ),
        migrations.AddField(
            model_name='opcao',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetos.Projeto'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='opcoes',
            field=models.ManyToManyField(help_text='Opcoes de projeto escolhidos', through='projetos.Opcao', to='projetos.Projeto'),
        ),
    ]
