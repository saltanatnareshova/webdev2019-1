from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import TaskList, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

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
    task_list = TaskListSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
