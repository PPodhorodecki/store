from django.urls import path

from . import views

app_name = 'sklep'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('/<int:pk>', views.product, name='product'),
]

