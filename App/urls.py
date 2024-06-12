from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy, Home

urlpatterns = [
    path('api/tasks/', TaskListCreate.as_view(), name='task-list-create'),  # Update URL here
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update-destroy'),  # Update URL here
    path('', Home.as_view(), name='home'),
]
