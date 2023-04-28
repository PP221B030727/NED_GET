from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(comments)
admin.site.register(ProductImage)
admin.site.register(Like)