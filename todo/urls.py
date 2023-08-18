from django.urls import path

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
]

app_name = "todo"
