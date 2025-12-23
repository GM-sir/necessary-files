from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('add_student/', views.add_student, name= 'add_student'),
    path('show_student/', views.show_student, name= 'show_student'),
    path('update_student/<int:id>', views.update_student, name= 'update_student'),
    path('delete_student/<int:id>', views.delete_student, name= 'delete_student'),
   
    path('sign_up/', views.sign_up, name= 'sign_up'),
    path('user_login/', views.user_login, name= 'user_login'),
    path('dashboard/', views.dashboard, name= 'dashboard'),
]
