from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Путь к странице авторизации
    path('logout/', views.logout_view, name='logout'),  # Путь к странице выхода
    path('home/', views.index, name='index'),  # Путь к главной странице
    path('insurances/', views.insurances, name='insurances'),  # Путь к странице со страховками
    path('detail_auto_insurance/<int:insurance_id>/', views.detail_auto_insurance, name='detail_auto_insurance'),
    # Путь к странице с детальной информацией об автостраховке
    path('detail_health_insurance/<int:insurance_id>/', views.detail_health_insurance, name='detail_health_insurance'),
    # Путь к странице с детальной информацией о медицинской страховке
    path('detail_property_insurance/<int:insurance_id>/', views.detail_property_insurance,
         name='detail_property_insurance'),
    path('create_auto_insurance/', views.create_auto_insurance, name='create_auto_insurance'),
    # Путь к странице создания автостраховки
    path('create_health_insurance/', views.create_health_insurance, name='create_health_insurance'),
    path('create_property_insurance/', views.create_property_insurance, name='create_property_insurance'),
    path('delete_auto_insurance/<int:insurance_id>/', views.delete_auto_insurance, name='delete_auto_insurance'),
    # Путь к странице удаления автостраховки
    path('delete_health_insurance/<int:insurance_id>/', views.delete_health_insurance, name='delete_health_insurance'),
    path('delete_property_insurance/<int:insurance_id>/', views.delete_property_insurance,
         name='delete_property_insurance'),
    path('update_auto_insurance/<int:insurance_id>/', views.update_auto_insurance, name='update_auto_insurance'),
    # Путь к странице обновления автостраховки
    path('update_health_insurance/<int:insurance_id>/', views.update_health_insurance, name='update_health_insurance'),
    path('update_property_insurance/<int:insurance_id>/', views.update_property_insurance,
         name='update_property_insurance'),
    path('register/', views.register, name='register'),  # Путь к странице создания клиента
    path('clients/', views.clients, name='clients'),  # Путь к странице со списком клиентов
    path('detail_client/<int:client_id>/', views.detail_client, name='detail_client'),
    # Путь к странице с детальной информацией о клиенте
    path('profile/<int:user_id>/', views.profile, name='profile'),  # Путь к странице профиля
    path('salary_report/', views.salary_report, name='salary_report'),  # Путь к странице отчета по зарплате
    path('agents/', views.agents, name='agents'),  # Путь к странице со списком агентов
    path('doc_auto_insurance/<int:insurance_id>/', views.doc_auto_insurance, name='doc_auto_insurance'),
    # Путь к странице с документами автостраховки
    path('doc_health_insurance/<int:insurance_id>/', views.doc_health_insurance, name='doc_health_insurance'),
    path('doc_property_insurance/<int:insurance_id>/', views.doc_property_insurance, name='doc_property_insurance'),
]
