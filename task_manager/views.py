from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View

from task_manager.forms import TaskForm
from task_manager.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "task_manager/index.html"


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task_manager:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task_manager:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task_manager:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:index")


class ChangeTaskStatusView(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        task.is_done = not task.is_done
        task.save()

        return redirect("task_manager:index")
