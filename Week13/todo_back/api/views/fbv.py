from api.models import TaskList
from api.serializers import TaskListSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def task_lists_view(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)


@api_view(['GET', 'PUT', 'DELETE'])
def task_list_view(request, pk):
    task_list = get_object_or_404(TaskList, pk=pk)
    if request.method == 'GET':
        serializer = TaskListSerializer(task_list)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        task_list.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def tasks_view(request, pk):
    if request.method == 'GET':
        task_list = get_object_or_404(TaskList, pk=pk)
        tasks = task_list.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        request.data['task_list'] = pk
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)
