from django.db import models
from fornecedores.models import Fornecedor

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.BigAutoField(primary_key=True, editable=False)
    titulo = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.titulo

class Produto(models.Model):
    id_produto = models.BigAutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    preco = models.FloatField(null=False, blank=False)
    data_entrada = models.DateTimeField(auto_now_add=True, null=True)
    data_validade = models.DateTimeField(null=True, blank=True)
    categoria_FK = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fornecedor_FK = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)