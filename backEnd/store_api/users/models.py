from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Funcao(models.Model):
    nome = models.CharField("Nome da funcao", max_length=100)
    descricao = models.TextField("Descricao da funcao", blank=True)
    def __str__(self):
        return self.nome

class Permissao(models.Model):
    nome = models.CharField("Nome da permissao", max_length=100)
    def __str__(self):
        return self.nome

class PermissaoFuncao(models.Model):
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, related_name='permissoes_funcao')
    permissao = models.ForeignKey(Permissao, on_delete=models.CASCADE, related_name='funcao_permissoes')
    class Meta:
        unique_together = ('funcao', 'permissao') #evita duplicatas
    def __str__(self):
        return f"{self.funcao.nome} - {self.permissao.nome}"

class Usuario(AbstractUser):
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, related_name='usuarios', null=True, blank=True)
    # Campos padrao de AbstractUser: username, email, password, etc.
    def __str__(self):
        return self.username