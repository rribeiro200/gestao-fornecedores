from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Fornecedor
from produtos.models import Produto
from django.core.exceptions import ValidationError
from django_select2.forms import Select2Widget
from collections import defaultdict




class FornecedorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Fornecedor
        fields = ('nome', 'cidade', 'estado', 'cep', 'contato', 'email', 'tipo',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'estado': Select2Widget(attrs={'class': 'form-select'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
            'contato': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DDD...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'tipo': Select2Widget(attrs={'class': 'form-select'}),
        }
    
    def clean_nome(self):
        nome = self.data.get('nome')

        if len(str(nome)) < 4:
            self.add_error('nome', 'Nome do fornecedor deve ter pelo menos 4 letras')
            
        return nome
    
    def clean_cidade(self):
        cidade = self.data.get('cidade')

        if len(str(cidade)) < 3:
            self.add_error('cidade', 'Informe uma cidade válida')

        return cidade
    
    def apenas_numeros(self, campo, erro):
        valor_do_campo = self.data.get(campo)
        try:
            valor_do_campo = int(valor_do_campo) # type: ignore
        except (ValueError, TypeError):
            self.add_error(campo, erro)

        return valor_do_campo
        
    def clean_cep(self):
        cep = 'cep'
        return self.apenas_numeros(cep, 'Digite um CEP válido.')
        
    def clean_contato(self):
        contato = 'contato'
        return self.apenas_numeros(contato, 'Digite um número de contato válido.')