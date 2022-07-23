from rest_framework import generics, filters
from .serializers import TodoSerializer
from .models import Todo
from django_filters.rest_framework import DjangoFilterBackend


class ListCreateTodoAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ["id", "title", "is_complete"]
    ordering_fields = ["id", "title", "is_complete"]
    search_fields = ["id", "title", "body", "is_complete"]

    def get_queryset(self):
        return Todo.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyTodoAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return Todo.objects.filter(creator=self.request.user)
