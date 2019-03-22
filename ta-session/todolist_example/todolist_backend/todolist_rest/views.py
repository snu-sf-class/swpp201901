from rest_framework import generics
from django.shortcuts import render
from todolist_rest.models import Todo
from todolist_rest.serializers import TodoSerializer

# Create your views here.
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
