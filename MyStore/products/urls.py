from django.urls import path
from products.views.main_views import products

app_name = 'products'
urlpatterns = [
    path('',products,name = 'index')


]
