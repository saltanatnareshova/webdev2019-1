from api.models import TaskList
from api.serializers import TaskListSerializer, TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class TaskListsView(APIView):
    def get(self, request):
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)


class TaskListView(APIView):
    def get(self, request, pk):
        task_list = get_object_or_404(TaskList, pk=pk)
        serializer = TaskListSerializer(task_list)
        return Response(serializer.data)

    def put(self, request, pk):
        task_list = get_object_or_404(TaskList, pk=pk)
        serializer = TaskListSerializer(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        task_list = get_object_or_404(TaskList, pk=pk)
        task_list.delete()
        return Response(status=204)


class TasksView(APIView):
    def get(self, request, pk):
        task_list = get_object_or_404(TaskList, pk=pk)
        tasks = task_list.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        request.data['task_list'] = pk
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)
