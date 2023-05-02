from django.urls import path
from products.views.cbv import *

app_name = 'products'
urlpatterns = [
    path('', ProductListAPIView.as_view()),
    path('<int:product_id>/', ProductDerailAPIView.as_view()),
]
