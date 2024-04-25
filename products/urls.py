from django.urls import path
from .views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, TagListCreateAPIView, TagRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(),
         name='product-list-create'),
    path('products/<int:pk>/',
         ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('tags/', TagListCreateAPIView.as_view(),
         name='tag-list-create'),
    path('tags/<int:pk>/',
         TagRetrieveUpdateDestroyAPIView.as_view(), name='tag-detail'),
]
