from django.urls import path, include

from .views import products_create, products_detail, products_upvote

urlpatterns = [
    path('create/', products_create, name='products-create-page'),
    path('<int:product_id>/', products_detail, name='products-detail-page'),
    path('<int:product_id>/upvote', products_upvote, name='products-upvote'),
]
