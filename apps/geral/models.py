from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    TIPO_CHOICES = (
        ('R', 'Receita'),
        ('D', 'Despesa')
    )
    nome = models.CharField(verbose_name='Nome', max_length=50)
    tipo = models.CharField(verbose_name='Tipo', max_length=1, choices=TIPO_CHOICES)
    descricao = models.TextField(verbose_name='Descricao', blank=True, null=True)

# Create your models here.
