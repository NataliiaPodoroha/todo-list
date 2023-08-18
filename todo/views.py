from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all()
    context_object_name = "task_list"
    template_name = "todo/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class ToggleTaskStatusView(generic.View):
    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)

        task.is_completed = not task.is_completed
        task.save()

        return HttpResponseRedirect(reverse_lazy("todo:task-list"))


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()
    context_object_name = "tag_list"
    template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
