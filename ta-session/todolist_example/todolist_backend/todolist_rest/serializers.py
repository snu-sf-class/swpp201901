from rest_framework import serializers
from todolist_rest.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('contents', 'done', 'id')
