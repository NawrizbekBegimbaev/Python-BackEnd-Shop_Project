from django.urls import path
from shop.views import *
from django.conf import settings
from django.conf.urls import static
from main import settings


urlpatterns = [
    path('<int:pk>/',shop_index,name='index'),
    path('',shop_list,name='shop'),
    path('cart/',cart_list,name='cart'),
    path('aboutus/',aboutus,name='about'),
    path('contact/',contact,name='contact'),
    path('cart/payment/',payment,name='pay'),
    path('search/',SearchView.as_view(),name='search'),
]
