from django.urls.conf import include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('measure_unit/', MeasureUnitListView.as_view(), name='measure_unit_list'),
    path('category_product/', CategoryProductListView.as_view(), name='category_product_list'),
    path('indicator/', IndicatorListView.as_view(), name='indicator_list'),
    path('', include(router.urls)),
]