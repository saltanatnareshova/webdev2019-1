from api.serializers import TaskListSerializer, TaskSerializer
from api import models

from django.views import View
from django.http import JsonResponse

from django.shortcuts import get_object_or_404
import json


class TaskLists(View):
    def get(self, request):
        task_lists = models.TaskList.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request):
        data = json.loads(request.body)
        serializer = TaskListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)


class TaskList(View):
    def get(self, request, pk):
        task_list = get_object_or_404(models.TaskList, pk=pk)
        serializer = TaskListSerializer(task_list)
        return JsonResponse(serializer.data, status=200)

    def put(self, request, pk):
        task_list = get_object_or_404(models.TaskList, pk=pk)
        data = json.loads(request.body)
        serializer = TaskListSerializer(instance=task_list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    def delete(self, request, pk):
        task_list = get_object_or_404(models.TaskList, pk=pk)
        task_list.delete()
        return JsonResponse({})


class Tasks(View):
    def get(self, request, pk):
        task_list = get_object_or_404(models.TaskList, pk=pk)
        tasks = task_list.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, pk):
        data = json.loads(request.body)
        data['task_list'] = pk
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)
