from django.contrib import admin
from products.models import *

admin.site.register(ProductCategory)
admin.site.register(ProductTag)
admin.site.register(Product)

