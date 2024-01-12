from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup.as_view(), name="signup"),
    path('services/', views.services, name='services'),
    path('materials/', views.materials, name='materials'),
    path('buy_materials/<int:pk>', views.BuyMaterials.as_view(), name='buy_materials'),
    path('edit_materials/<int:pk>', views.EditMaterials.as_view(), name='edit_materials'),
    path('write_offs/<int:pk>', views.CreateWrite_offs.as_view(), name='write_offs'),
    path('create_order/<int:pk>', views.CreateOrder.as_view(), name='create_order'),
    path('profile/<int:pk>', views.Profile.as_view(), name='profile'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('please_login/', views.please_login, name='please_login'),
    path('orders/', views.orders, name='orders'),
    path('delete_order/<int:pk>', views.DeleteOrder.as_view(), name='delete_order'),
    path('edit_order/<int:pk>', views.EditOrder.as_view(), name='edit_order'),
]
