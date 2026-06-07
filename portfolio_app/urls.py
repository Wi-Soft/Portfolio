
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('education/', views.education, name='education'),
    path('about/', views.education, name='about'),
    path('contact/', views.education, name='contact'),
    path('header/', views.education, name='header'),
    path('projcet/', views.education, name='project'),
    path('skills/', views.education, name='skils')
]
