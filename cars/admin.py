from django.contrib import admin
from cars.models import Brand, Car

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name', )

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'created_at')
    search_fields = ('name', 'brand__name',)