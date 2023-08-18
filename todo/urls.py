from django.urls import path

from todo.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    ToggleTaskStatusView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path(
        "/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "/<int:pk>/toggle-status/",
        ToggleTaskStatusView.as_view(),
        name="toggle-task-status",
    ),
]

app_name = "todo"
