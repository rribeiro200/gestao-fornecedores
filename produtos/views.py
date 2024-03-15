from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def novo_produto(request, pk):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Produto criado com sucesso.')
                return redirect('fornecedores:detalhes_fornecedor', pk=pk)
            except Exception as e:
                messages.error(request, f'Erro ao criar produto {e}')
        else:
            ctx = {'form': form}
            return render(request, 'produtos/novo_produto.html', ctx)
    
    form = ProdutoForm()
    
    ctx = {'form': form}

    return render(request, 'produtos/novo_produto.html', ctx)