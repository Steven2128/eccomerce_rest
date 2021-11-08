from django.urls import path
from .views import *

urlpatterns = [
    path('', user_list_view, name='usuario_list')
]