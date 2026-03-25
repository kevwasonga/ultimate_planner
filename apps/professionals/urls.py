from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('professionals/', views.professionals_list, name='professionals_list'),
    path('professionals/<int:pk>/', views.professional_detail, name='professional_detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
