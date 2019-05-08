from django.urls import path
from api import views
from django.views.decorators.csrf import csrf_exempt

# old_views
# urlpatterns = [
#     path('task_lists', csrf_exempt(views.TaskLists.as_view())),
#     path('task_lists/<int:pk>', csrf_exempt(views.TaskList.as_view())),
#     path('task_lists/<int:pk>/tasks', csrf_exempt(views.Tasks.as_view()))
# ]

# fbv
# urlpatterns = [
#     path('task_lists', views.task_lists_view),
#     path('task_lists/<int:pk>', views.task_list_view),
#     path('task_lists/<int:pk>/tasks', views.tasks_view)
# ]

# cbv
urlpatterns = [
    path('task_lists', views.TaskListsView.as_view()),
    path('task_lists/<int:pk>', views.TaskListView.as_view()),
    path('task_lists/<int:pk>/tasks', views.TasksView.as_view()),
    path('users', views.UserList.as_view()),
    path('login', views.Login.as_view()),
    path('logout', views.Logout.as_view())
]
