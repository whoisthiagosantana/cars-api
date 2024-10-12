from rest_framework import serializers
from cars.models import Brand, Car

class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
        model = Brand
        fields = '__all__'

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
        model = Car
        fields = '__all__'
