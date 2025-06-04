from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField("Categoria", max_length=100)
    descricao = models.TextField("Descricao", blank=True)
    def __str__(self):
        return self.nome
    
class Marca(models.Model):
    nome = models.CharField("Marca", max_length=100)
    descricao = models.TextField("Descricao", blank=True)
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='produtos')
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='produtos')
    nome = models.CharField("Nome do produto", max_length=255)
    descricao = models.TextField("Descricao", blank=True)
    quantidade = models.IntegerField("Quantidade em estoque", default=0)
    preco = models.DecimalField("Preco", max_digits=10, decimal_places=2)
    status = models.CharField("Status", max_length=20, default='activo')
    codigo_barra = models.CharField("Código de barras", max_length=50, unique=True)
    avaliacao = models.DecimalField("Avaliacao", max_digits=3, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return self.nome
