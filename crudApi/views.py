from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.

class ProductView(APIView):
    # get products
    def get(self, request, format=None):
        try:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=200)
        except Product.DoesNotExist:
            return Response(serializer.errors, status=400)

    # create product
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class ProductDetailView(APIView):
    # get product based on id
    def get(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    # update product
    def put(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    # delete product
    def delete(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=200)