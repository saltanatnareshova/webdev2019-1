from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.shortcuts import get_object_or_404


class TaskListsView(generics.ListCreateAPIView):
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TasksView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(task_list=self.kwargs['pk'])

    def perform_create(self, serializer):
        task_list = get_object_or_404(TaskList, id=self.kwargs['pk'])
        serializer.save(task_list=task_list)
