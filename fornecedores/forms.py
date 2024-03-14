from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Fornecedor
from produtos.models import Produto
from django.core.exceptions import ValidationError


class FornecedorForm(forms.ModelForm):
    def __init__(self, data):
        super().__init__(data)

    class Meta:
        model = Fornecedor
        fields = ('nome', 'cidade', 'estado', 'cep', 'contato', 'email', 'tipo',)
        widgets = {

        }

    def save(self, commit=True):
        fornecedor = super().save(commit=False)
        if commit:
            # Salva definitivamente o FORMULÁRIO no BANCO DE DADOS
            fornecedor.save()
                    
        return fornecedor