from django.urls import path
from .views import *
urlpatterns = [
    path('measure_unit/', MeasureUnitListView.as_view(), name='measure_unit_list'),
    path('category_product/', CategoryProductListView.as_view(), name='category_product_list'),
    path('indicator/', IndicatorListView.as_view(), name='indicator_list'),
    path('product/', ProductListCreateView.as_view(), name='product_create'),
    path('product/<int:pk>', ProductRetrieveUpdateDestroyview.as_view(), name='product_retrieve'),
]