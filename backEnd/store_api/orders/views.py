#from django.shortcuts import render
from rest_framework import viewsets
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
