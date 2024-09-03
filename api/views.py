from django.shortcuts import render
from rest_framework import viewsets, permissions

from api.custom_pagination import CustomPagination
from api.models import Product
from api.serializers import ProductSerializer, ProductListSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny,]
    pagination_class = CustomPagination

    def get_queryset(self):
        # list random products each refresh request time
<<<<<<< HEAD
        return Product.objects.order_by('?')[0:200]
=======
        return Product.objects.order_by('?')[:200]
>>>>>>> origin/main
