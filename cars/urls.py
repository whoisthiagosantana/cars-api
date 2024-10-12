# filtros RQL, estudar, tem haver com os filtros
# swagger para django pesquise por drf-yasg

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cars.views import BrandModelViewSet, CarModelViewSet

## Com django e DRF, vc usa ClassBasedViews, ModelViewSet

router = DefaultRouter()
router.register('brands', BrandModelViewSet)
router.register('cars', CarModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
