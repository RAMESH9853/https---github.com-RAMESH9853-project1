from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductMainModel
from rest_framework import generics
from .serializers import ProductMainSerializer

class ProductMainList(generics.ListAPIView):
    queryset = ProductMainModel.objects.all()
    serializer_class = ProductMainSerializer

class ProductMainDetail(generics.RetrieveAPIView):
    queryset = ProductMainModel.objects.all()
    serializer_class = ProductMainSerializer
