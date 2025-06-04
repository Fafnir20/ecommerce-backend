from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet, ItemPedidoViewSet, TransacaoViewSet, TipoTransacaoViewSet

router = DefaultRouter()
router.register('pedidos', PedidoViewSet)
router.register('itempedidos', ItemPedidoViewSet)
router.register('transacoes', TransacaoViewSet)
router.register('tipotransacoes', TipoTransacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]