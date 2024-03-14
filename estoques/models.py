from django.db import models
from produtos.models import Produto
from fornecedores.models import Fornecedor

# Create your models here.
class Estoque(models.Model):
    id_estoque = models.BigAutoField(primary_key=True, editable=True)
    quantidade = models.IntegerField(null=False, blank=False)
    produto_FK = models.ForeignKey(Produto, on_delete=models.CASCADE, null=False, blank=False)
    fornecedor_FK = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)