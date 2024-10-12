from dj_rql.drf import RQLFilterBackend
from rest_framework import viewsets, generics, permissions
from cars.models import Brand, Car
from cars.permissions import CarOwnerPermission
from cars.serializers import BrandModelSerializer, CarModelSerializer
from cars.filters import BrandFilterClass, CarFilterClass

class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = BrandFilterClass

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = CarFilterClass
    permission_classes = [permissions.DjangoModelPermissions, CarOwnerPermission,]
    # Subscreve os settings permitindo que a classe tenha permissão full para todos (api aberta ou qualquer regra)
    # permission_classes = [permissions.AllowAny]


#class CarCreateView(generics.CreateAPIView):
#    queryset = Car.objects.all()
#    serializer_class = CarModelSerializer
#    filter_backends = [RQLFilterBackend]
#    rql_filter_class = CarFilterClass

#class CarUpdateView(generics.UpdateAPIView):
#    queryset = Car.objects.all()
#    serializer_class = CarModelSerializer
#    filter_backends = [RQLFilterBackend]
#    rql_filter_class = CarFilterClass

#class CarListView(generics.ListAPIView):
#    queryset = Car.objects.all()
#    serializer_class = CarModelSerializer
#    filter_backends = [RQLFilterBackend]
#    rql_filter_class = CarFilterClass

