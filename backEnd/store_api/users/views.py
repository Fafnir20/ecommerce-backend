from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Funcao, Permissao, Endereco
from .serializers import UsuarioSerializer, FuncaoSerializer, PermissaoSerializer, EnderecoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def get_queryset(self):
        # opcional: filtrar por usuário autenticado
        user = self.request.user
        return Endereco.objects.filter(usuario=user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

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
