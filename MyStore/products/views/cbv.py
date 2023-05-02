from django.shortcuts import Http404
from rest_framework import status
from products.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ModelProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ModelProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDerailAPIView(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ModelProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, product_id):
        instance = self.get_object(product_id)
        serializer = ModelProductSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,product_id):
        print(product_id)
        instance = self.get_object(product_id)
        instance.delete()
        return Response({'deleted': True})


