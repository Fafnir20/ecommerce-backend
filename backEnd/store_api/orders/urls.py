from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet, ItemPedidoViewSet, TransacaoViewSet, TipoTransacaoViewSet, TopProdutosByOrdersView

router = DefaultRouter()
router.register('pedidos', PedidoViewSet)
router.register('itempedidos', ItemPedidoViewSet)
router.register('transacoes', TransacaoViewSet)
router.register('tipotransacoes', TipoTransacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Nova rota de relatório de Top Products
    path('top-products/', TopProdutosByOrdersView.as_view(), name='top-products-by-orders'),
]