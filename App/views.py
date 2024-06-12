from rest_framework import generics
from App.models import Task
from App.serializers import TaskSerializer
from django.shortcuts import render
from django.views import View



class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class Home(View):
    def get(self, request):
        return render(request, "index.html")

