from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('groups/', views.groups, name='groups'),
    path('programs/', views.programs, name='programs'),
    path('add_program/', views.add_program, name='add_program'),
    path('edit_program/<int:program_id>/', views.edit_program, name='edit_program'),
    path('delete_program/<int:program_id>/', views.delete_program, name='delete_program'),
    path('add_group/', views.add_group, name='add_group'),
    path('edit_group/<int:group_id>/', views.edit_group, name='edit_group'),
    path('delete_group/<int:group_id>/', views.delete_group, name='delete_group'),
    path("instructors/", views.instructors, name="instructors"),
    path("students/", views.students, name="students"),
    path("add_student/", views.add_student, name="add_student"),
    path("group/<int:group_id>/", views.group, name="group"),
    path("exams/", views.exams, name="exams"),
    path("add_exam/", views.add_exam, name="add_exam"),
    path("edit_exam/<int:exam_id>/", views.edit_exam, name="edit_exam"),
    path("delete_exam/<int:exam_id>/", views.delete_exam, name="delete_exam"),
    path("results_exams/", views.results_exams, name="results_exams"),
    path("create_results_exams/", views.create_results_exams, name="create_results_exams")
]
