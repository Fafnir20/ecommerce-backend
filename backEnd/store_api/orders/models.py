from django.db import models
from django.conf import settings
from django.utils import timezone


class Pedido(models.Model):
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pedidos')
    status = models.CharField("Status do pedido", max_length=20, default='pendente')
    data_pedido = models.DateTimeField("Data do pedido", default=timezone.now)
    valor_total = models.DecimalField("Valor total", max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Pedido {self.id} -  Cliente {self.cliente.username}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey('products.Produto', on_delete=models.PROTECT, related_name='itens_pedido')
    quantidade = models.IntegerField("Quantidade")
    preco_unitario = models.DecimalField("Preco unitario", max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"

class TipoTransacao(models.Model):
    nome = models.CharField("Tipo de transacao", max_length=50)
    descricao = models.TextField("Descricao", blank=True)
    def __str__(self):
        return self.nome


class Transacao(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='transacoes')
    tipo = models.ForeignKey(TipoTransacao, on_delete=models.PROTECT, related_name='transacoes')
    qtd_produtos = models.IntegerField("Quantidade de produtos")
    valor_transacao = models.DecimalField("Valor da transacao", max_digits=10, decimal_places=2)
    data_transacao = models.DateTimeField("Data da Transacao", default=timezone.now)
    status = models.CharField("Status da transacao", max_length=20, default='iniciada')
    def __str__(self):
        return f"Transacao {self.id} - Pedido {self.pedido.id}"
     

# Create your models here.
