from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from .models import *
from .serializers import *

class MeasureUnitListView(ListAPIView):
    serializer_class = MeasureUnitSerializer
    queryset = MeasureUnit.objects.filter(state=True)
        
class CategoryProductListView(ListAPIView):
    serializer_class = CategoryProductSerializer
    queryset = CategoryProduct.objects.filter(state=True)
    
class IndicatorListView(ListAPIView):
    serializer_class = IndicatorSerializer
    queryset = Indicator.objects.filter(state=True)

class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(state=True)
    
class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer
    
class ProductRetrieveview(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
class ProductDestroyview(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
class ProductUpdateview(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()