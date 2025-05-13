from django.db import models
from django.contrib.auth.models import AbstractUser

# Usuário personalizado com papéis
class Usuario(AbstractUser):
    TIPO_USUARIO = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('responsavel', 'Responsável'),
        ('diretor', 'Diretor'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO)

class Aluno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20)
    turma = models.CharField(max_length=20)

class Professor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    disciplina = models.CharField(max_length=100)

class Avaliacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    nota = models.FloatField()
    data = models.DateField()

class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data = models.DateField()
    presente = models.BooleanField(default=False)
