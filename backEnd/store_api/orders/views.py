#from django.shortcuts import render
from rest_framework import viewsets, generics
from django.db.models import Sum
from products.models import Produto
from products.serializers import TopProdutoSerializer
from .models import Pedido, ItemPedido, Transacao, TipoTransacao
from .serializers import PedidoSerializer, ItemPedidoSerializer, TransacaoSerializer, TipoTransacaoSerializer


# Create your views here.

class TipoTransacaoViewSet(viewsets.ModelViewSet):
    queryset = TipoTransacao.objects.all()
    serializer_class = TipoTransacaoSerializer


class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer


class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class TopProdutosByOrdersView(generics.ListAPIView):
    """
    Retorna os produtos mais vendidos, agregando pelo ItemPedido.
    """
    serializer_class = TopProdutoSerializer

    def get_queryset(self):
        # Anota cada Produto com total_vendido (soma de ItemPedido.quantidade)
        return (
            Produto.objects
                   .annotate(total_vendido=Sum('itens_pedido__quantidade'))
                   .order_by('-total_vendido')
        )


