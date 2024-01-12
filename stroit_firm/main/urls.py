from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views
from django.urls.resolvers import URLPattern

urlpatterns = [
    path('signup/', views.signup.as_view(), name="signup"),
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('add_to_cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('delete_from_cart/<int:pk>', views.delete_from_cart, name='delete_from_cart'),
    path('orders/', views.sales, name='sales'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('add_material/', views.add_material.as_view(), name='add_material'),
    path('edit_material/<int:pk>', views.edit_material.as_view(), name='edit_material'),
    path('delete_material/<int:pk>', views.delete_material.as_view(), name='delete_material'),
]
