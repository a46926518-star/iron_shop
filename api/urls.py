from django.urls import path
from . import views

urlpatterns = [
    path('mahsulotlar/', views.ProductListView.as_view(), name='product-list'),
    path('kategoriyalar/', views.CategoryListView.as_view(), name='category-list'),

    path('register/', views.RegisterView.as_view(), name='auth_register'),

    path('cart/', views.CartListView.as_view(), name='cart-list'),
]