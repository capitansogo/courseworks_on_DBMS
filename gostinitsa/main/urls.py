from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.rooms, name='rooms'),
    path('room/<int:pk>/', views.room, name='room'),
    path("signup/", views.signup.as_view(), name="signup"),
    path('add_bron/<int:pk>', views.add_bron, name='add_bron'),
    path('edit_room/<int:pk>', views.edit_room.as_view(), name='edit_room'),
    path('users/', views.users, name='users'),
    path('bron_update/<int:pk>', views.bron_update.as_view(), name='bron_update'),
    path('bron_delete/<int:pk>', views.bron_delete.as_view(), name='bron_delete'),
    path('free_nomers/', views.free_nomers, name='free_nomers'),
]
