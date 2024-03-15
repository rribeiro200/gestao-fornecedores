from django.urls import path, include
from . import views

app_name = 'produtos'

urlpatterns = [
    path('novo_produto/<int:pk>/', views.novo_produto, name='novo_produto'),
]