
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('education/', views.education, name='education'),
    path('contact/', views.contact, name='contact'),
    path('header/', views.header, name='header'),
    path('project/', views.project, name='project'),
    path('skills/', views.skills, name='skills'),
    path('experience/', views.experience, name='experience'),
    
]
