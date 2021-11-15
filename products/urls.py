from django.urls import path
from .views import *
urlpatterns = [
    path('measure_unit/', MeasureUnitListView.as_view(), name='measure_unit_list'),
    path('category_product/', CategoryProductListView.as_view(), name='category_product_list'),
    path('indicator/', IndicatorListView.as_view(), name='indicator_list'),
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
]