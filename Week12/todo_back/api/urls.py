from django.urls import path
from api import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('task_lists/', csrf_exempt(views.TaskLists.as_view())),
    path('task_lists/<int:pk>/', csrf_exempt(views.TaskList.as_view())),
    path('task_lists/<int:pk>/tasks', csrf_exempt(views.Tasks.as_view()))
]
