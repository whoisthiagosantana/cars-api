from django.db import models

from contrib.models import TableBaseModel

class Brand(TableBaseModel):
    pass

    def __str__(self):
        return self.name
    
    class Meta:

        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_%(class)s_name'),
        ]

        verbose_name_plural = 'Brands'
        verbose_name = 'Brand'
        db_table = 'cars_brand'
        ordering = ['name']

class Car(TableBaseModel):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=False, blank=False)
    factory_year = models.IntegerField(null=True)
    model_year = models.IntegerField(null=True)
    color = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return self.name + ' - ' + self.brand.name
    
    class Meta:

        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_%(class)s_name'),
        ]

        verbose_name_plural = 'Cars'
        verbose_name = 'Car'
        db_table = 'cars_car'
        ordering = ['name']