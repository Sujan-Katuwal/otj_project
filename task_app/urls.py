from django.urls import path
from .import views

urlpatterns = [
    path('task_api/<int:pk>/', views.task_api, name="task_api"),
    path('task_api/', views.task_api, name="task_api" ),
    path('create_task/', views.create_task, name="create_task"),
    path('update_task/<int:pk>/', views.update_task, name="update_task"),
    path('update_task/', views.update_task, name="update_task"),
    path('delete_task/<int:pk>/', views.delete_task, name="delete_task"),
    path('delete_task/', views.delete_task, name="delete_task"),
    path('mark_task_completed/<int:pk>/', views.mark_task_completed, name="mark_task_completed"),
    path('mark_task_completed/', views.mark_task_completed, name="mark_task_completed"),
    path('add_task/', views.add_task, name="add_task"),
    path('task_list/', views.task_list, name="task_list"),

]
