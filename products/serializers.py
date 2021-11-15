from django.db.models import fields
from .models import MeasureUnit, CategoryProduct, Indicator, Product
from rest_framework import serializers
from .serializers import *


class MeasureUnitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeasureUnit
        exclude = ('state', 'created_date', 'modified_date', 'delete_date')
        
class CategoryProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoryProduct
        exclude = ('state', 'created_date', 'modified_date', 'delete_date')
        
class IndicatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Indicator
        exclude = ('state', 'created_date', 'modified_date', 'delete_date')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'delete_date')