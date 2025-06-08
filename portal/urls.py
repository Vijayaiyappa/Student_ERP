from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home_view, name='home'),
    path('save_ajax/', views.save_student_ajax, name='save_ajax'),
    path('edit_ajax/', views.edit_student_ajax, name='edit_ajax'),
    path('delete_ajax/', views.delete_student_ajax, name='delete_ajax'),
]