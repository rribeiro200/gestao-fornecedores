from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'descricao', 'preco', 'data_validade', 'categoria_FK', 'fornecedor_FK')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
            'data_validade': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'categoria_FK': forms.Select(attrs={'class': 'form-select'}),
            'fornecedor_FK': forms.Select(attrs={'class': 'form-select'}),
        }