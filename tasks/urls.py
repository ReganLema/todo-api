from django.urls import path

from .views import (
    TaskListCreateView,
    TaskDetailView,
    CompleteTaskView,
)

urlpatterns = [

    path(
        "",
        TaskListCreateView.as_view(),
        name="task-list",
    ),

    path(
        "<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail",
    ),


     path(
        "<int:pk>/complete/",
        CompleteTaskView.as_view(),
    ),
]