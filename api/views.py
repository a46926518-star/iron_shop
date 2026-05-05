# Create your views here.
from rest_framework import generics, permissions
from .models import Category, Product, Order, CartItem
from .serializers import (
    CategorySerializer, ProductSerializer, OrderSerializer,
    CartItemSerializer, RegisterSerializer
)

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class CartListView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)