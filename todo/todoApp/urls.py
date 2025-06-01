from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.todo_list, name="todo_list"),
    path('create/', views.create_todo, name="create_todo"),
    path('complete/<int:todo_id>/', views.complete_todo, name="complete_todo"),
     path('update/<int:todo_id>/', views.update_todo, name="update_todo"),
    path('delete/<int:todo_id>/', views.delete_todo, name="delete_todo"),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
