from django.urls import path
from .views import ProductView, ProductDetailView

urlpatterns = [
    path('product/', ProductView.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view()),
]