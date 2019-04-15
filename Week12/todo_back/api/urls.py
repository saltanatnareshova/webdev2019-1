from django.urls import path
from api import views

urlpatterns = [
    path('task_lists/', views.task_lists),
    path('task_lists/<int:pkey>/', views.task_list),
    path('task_lists/<int:pkey>/tasks', views.tasks)
]