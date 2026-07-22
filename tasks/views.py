from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView



class TaskListCreateView(generics.ListCreateAPIView):

    serializer_class = TaskSerializer

    permission_classes = [permissions.IsAuthenticated]

    queryset = Task.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "completed",
    ]

    search_fields = [
        "title",
        "description",
    ]

    ordering_fields = [
        "created_at",
        "title",
    ]

    def get_queryset(self):
        return Task.objects.filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)





class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TaskSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)







class CompleteTaskView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):

        task = generics.get_object_or_404(
            Task,
            pk=pk,
            owner=request.user,
        )

        task.completed = True

        task.save()

        return Response(
            {
                "message": "Task marked as completed."
            },
            status=status.HTTP_200_OK,
        )