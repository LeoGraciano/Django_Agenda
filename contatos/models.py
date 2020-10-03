from django.utils import timezone
from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=250)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=250)
    sobrenome = models.CharField(max_length=250, blank=True)
    telefone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, blank=True)
    data_da_criação = models.DateTimeField(default=timezone.now)
    descrição = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
