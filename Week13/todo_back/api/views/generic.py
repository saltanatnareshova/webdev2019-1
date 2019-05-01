from api.models import TaskList
from api.serializers import TaskListSerializer, TaskSerializer
from rest_framework import generics


class TaskListsView(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
