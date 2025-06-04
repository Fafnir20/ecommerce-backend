from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Funcao, Permissao
from .serializers import UsuarioSerializer, FuncaoSerializer, PermissaoSerializer

class FuncaoViewSet(viewsets.ModelViewSet):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer


class PermissaoViewSet(viewsets.ModelViewSet):
    queryset = Permissao.objects.all()
    serializer_class = PermissaoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    
# Create your views here.
