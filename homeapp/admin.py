from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(CustomerModel)
admin.site.register(CategoryModel)
admin.site.register(ProductModel)