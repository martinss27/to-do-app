from django.shortcuts import render
from rest_framework import generics
from .serializers import ToDoSerializer
from .models import ToDo

# Create your views here.
# todo o processo de CRUD aqui

class ListTodo(generics.ListAPIView):  # READ
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailTodo(generics.RetrieveDestroyAPIView):  # UPDATE
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView):  # CREATE
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteTodo(generics.DestroyAPIView):  # DELETE
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer