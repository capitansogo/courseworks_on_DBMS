from . import views
from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('teams_champions/', views.teams_champions, name='teams_champions'),
    path('teams_europe/', views.teams_europe, name='teams_europe'),
    path('teams/<int:team_id>/', views.team, name='team'),
    path('player/<int:player_id>/', views.player, name='player'),
    path('matches_champions/', views.matches_champions, name='matches_champions'),
    path('matches_europe/', views.matches_europe, name='matches_europe'),
    path('match/<int:match_id>/', views.match, name='match'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('match/edit/<int:match_id>/', views.edit_match, name='edit_match'),
    path('match/delete/<int:match_id>/', views.delete_match, name='delete_match'),
    path('match/add/', views.add_match, name='add_match'),
]
