from rest_framework import serializers
from .models import Pedido, ItemPedido, Transacao, TipoTransacao

class TipoTransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTransacao
        fields = '__all__'

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = '__all__'


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = '__all__'
        
class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True, read_only=True)
    transacoes = TransacaoSerializer(many=True, read_only=True)
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'status', 'data_pedido', 'valor_total', 'itens', 'transacoes']





