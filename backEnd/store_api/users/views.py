from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Funcao, Permissao, Endereco
from .serializers import UsuarioSerializer, FuncaoSerializer, PermissaoSerializer, EnderecoSerializer
from rest_framework.permissions import IsAuthenticated

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = [IsAuthenticated]  # Garante que apenas usuários autenticados possam acessar

    def get_queryset(self):
         return Endereco.objects.filter(usuario=self.request.user)
        
    
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
