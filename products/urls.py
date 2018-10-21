from django.urls import path, include

from .views import products_create

urlpatterns = [
    path('create/', products_create, name='products-create-page'),
]
