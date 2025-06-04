from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, MarcaViewSet, ProdutoViewSet


router = DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('marcas', MarcaViewSet)
router.register('produtos', ProdutoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
