from django.http import JsonResponse
from api.models import TaskList, Task

def task_lists(request):
    task_lists = TaskList.objects.all()
    json_task_lists = [tl.to_json() for tl in task_lists]
    return JsonResponse(json_task_lists, safe=False)

def task_list(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(task_list.to_json())

def tasks(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = task_list.task_set.all()
    json_tasks = [task.to_json() for task in tasks]
    return JsonResponse(json_tasks, safe=False)
