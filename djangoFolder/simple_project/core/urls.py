from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home),
    path('add_student/', views.add, name='add'),
    path('all_student/', views.all, name='all'),
]