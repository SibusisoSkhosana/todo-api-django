import logging
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

logger = logging.getLogger(__name__)

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        todo = serializer.save()
        logger.info(f"Todo created: {todo.id} - {todo.title}")

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_update(self, serializer):
        todo = serializer.save()
        logger.info(f"Todo updated: {todo.id}")

    def perform_destroy(self, instance):
        logger.info(f"Todo deleted: {instance.id}")
        instance.delete()
