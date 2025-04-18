from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    # path('tasks/', views.task_list, name='task_list'),
    # path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:pk>/update/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    
]