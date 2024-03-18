from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fornecedor
from produtos.models import Produto
from .forms import FornecedorForm
from django.contrib import messages
from utils.valida_edicao_fornecedor import valida_edicao_fornecedor

# Create your views here.
def index(request):
    
    return render(request, 'fornecedores/index.html')


def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.filter()

    ctx = {
        'fornecedores': fornecedores
    }

    return render(request, 'fornecedores/lista_fornecedores.html', ctx)


def detalhes_fornecedor(request, pk):
    fornecedor = Fornecedor.objects.filter(id_fornecedor=pk).first()
    produto_fornecedor = Produto.objects.filter(fornecedor_FK=fornecedor)
    print('Fornecedor:          ', fornecedor)
    print('Produtos do Fornecedor:          ', produto_fornecedor)
    
    ctx = {'fornecedor': fornecedor, 'produto_fornecedor': produto_fornecedor}
    return render(request, 'fornecedores/detalhes_fornecedor.html', ctx)


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


def editar_fornecedor(request, pk):
    fornecedor = Fornecedor.objects.filter(pk=pk).first()
    produto_fornecedor = Produto.objects.filter(fornecedor_FK=pk)
    tipos_fornecedor = Fornecedor.objects.values_list('tipo', flat=True).distinct()

    if request.method == 'POST':
        dados_para_edicao = request.POST
        valida_edicao_fornecedor(fornecedor, dados_para_edicao)

        return redirect('fornecedores:editar_fornecedor', pk=pk)

    ctx = {
        'fornecedor': fornecedor,
        'produto_fornecedor': produto_fornecedor,
        'tipos_fornecedor': tipos_fornecedor
    }

    return render(request, 'fornecedores/editar_fornecedor.html', ctx)