from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fornecedor
from .forms import FornecedorForm
from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request, 'fornecedores/index.html')


def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.filter()

    ctx = {
        'fornecedores': fornecedores
    }

    return render(request, 'fornecedores/lista_fornecedores.html', ctx)


def adicionar_fornecedor(request):
    if request.method == "POST":
        form = FornecedorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Fornecedor criado com sucesso.')
                return redirect('fornecedores:adicionar_fornecedor')
            except Exception as e:
                messages.error(request, f'Erro ao criar fornecedor {e}')
        else:
            ctx = {'form': form}
            return render(request, 'fornecedores/adicionar_fornecedor.html', ctx)
    
    form = FornecedorForm()
    
    ctx = {'form': form}

    return render(request, 'fornecedores/adicionar_fornecedor.html', ctx)