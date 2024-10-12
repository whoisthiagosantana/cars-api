from dj_rql.filter_cls import AutoRQLFilterClass, FilterLookups
from cars.models import Brand, Car

# Exemplos: http://127.0.0.1:8000/api/v1/brands/?eq(name,Suzuki)
# Exemplos: http://127.0.0.1:8000/api/v1/brands/?ilike(name,*s*)
class BrandFilterClass(AutoRQLFilterClass):
    MODEL = Brand

# Exemplos: http://127.0.0.1:8000/api/v1/cars/?ilike(name,fusca)&ge(factory_year,1970)
# Exemplos: http://127.0.0.1:8000/api/v1/cars/?ordering(-factory_year)
# Exemplos com filtros: http://127.0.0.1:8000/api/v1/cars/?ilike(brand,*suzu*)
class CarFilterClass(AutoRQLFilterClass):
    MODEL = Car
    FILTERS = [
        {
            'filter': 'brand',
            'source': 'brand__name',
        },
        {
            'filter': 'user',
            'source': 'user__username',
        }
    ]