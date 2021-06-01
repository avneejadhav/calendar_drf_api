from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        def validate(self, data):
        
            if data['start_time'] > data['end_time'] or data['start_time'] == data['end_time']:
                raise serializers.ValidationError("end_time must occur after start_time")
            return data