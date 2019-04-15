from django.db import models


class TaskList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    due_on = models.DateTimeField()
    status = models.CharField(max_length=40)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return 'Task list: {}\n{}: {}\nStatus: {}'.format(self.task_list.name, self.id, self.name, self.status)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.strftime('%d.%m.%Y %H:%M'),
            'due_on': self.due_on.strftime('%d.%m.%Y %H:%M'),
            'status': self.status,
            'task_list': self.task_list.name
        }
