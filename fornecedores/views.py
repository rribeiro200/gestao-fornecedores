from django.shortcuts import render
from django.http import HttpResponse
from .models import Fornecedor
from .forms import FornecedorForm

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
    form = FornecedorForm(data=None)

    if request.method == "POST":
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()

    ctx = {
        'form': form
    }
    return render(request, 'fornecedores/adicionar_fornecedor.html', ctx)