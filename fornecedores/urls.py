from django.urls import path, include
from . import views

app_name = 'fornecedores'

urlpatterns = [
    path('', views.index, name='index'),
    path('fornecedores/', views.lista_fornecedores, name='lista_fornecedores'),
    path('adicionar_fornecedor/', views.adicionar_fornecedor, name='adicionar_fornecedor'),
    path('detalhes_fornecedor/<int:pk>/', views.detalhes_fornecedor, name='detalhes_fornecedor'),
]
