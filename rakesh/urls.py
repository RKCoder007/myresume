from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('resume/', views.resume_page, name='resume'),
    path('services/', views.services_page, name='services'),
    path('projects/', views.projects_page, name='projects'),
    path('contact/', views.contact_page, name='contact'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_page, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('projectDetails/<str:pk>/', views.proj_details_page, name='project details'),
    path('create_proj/', views.create_proj, name='create_proj'),
    path('update_proj/<str:pk>/', views.update_proj, name='update_proj'),
    path('delete_proj/<str:pk>/', views.delete_proj, name='delete_proj'),
    path('web_content_form/<str:pk>/', views.update_web_content_form, name='web_content_form'),
]
