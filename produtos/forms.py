from django import forms
from .models import Produto
from django.core.exceptions import ValidationError


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'descricao', 'preco', 'data_entrada', 'data_validade', 'categoria_FK')
        widgets = {
            
        }

    def clean(self):
        super_clean = super().clean()
        

        return super_clean