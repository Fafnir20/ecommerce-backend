#from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Marca, Produto
from .serializers import CategoriaSerializer, MarcaSerializer, ProdutoSerializer

# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer



