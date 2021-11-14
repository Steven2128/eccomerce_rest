from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *

class MeasureUnitListView(ListAPIView):
    serializer_class = MeasureUnitSerializer
    
    def get_queryset(self):
        return MeasureUnit.objects.filter(state=True)
        
class CategoryProductListView(ListAPIView):
    serializer_class = CategoryProductSerializer
    
    def get_queryset(self):
        return CategoryProduct.objects.filter(state=True)
    
class IndicatorListView(ListAPIView):
    serializer_class = IndicatorSerializer
    
    def get_queryset(self):
        return Indicator.objects.filter(state=True)