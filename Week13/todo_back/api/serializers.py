from rest_framework import serializers
from api.models import TaskList, Task


class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        task_list = TaskList(**validated_data)
        task_list.save()
        return task_list

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(read_only=True)
    due_on = serializers.DateTimeField(read_only=True)
    status = serializers.CharField(default='TODO')
    task_list = serializers.PrimaryKeyRelatedField(queryset=TaskList.objects.all())

    class Meta:
        model = Task
        fields = '__all__'
