from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from Mixin import TaskPassesTestMixin
from tasks.forms import TaskForm
from tasks.models import Task

from django.shortcuts import render


def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})


class CreateTaskView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks')
    success_message = 'Task create!'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.author = self.request.user
        form.instance.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdateTaskView(TaskPassesTestMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks')
    success_message = 'Task update!'


class DeleteTaskView(TaskPassesTestMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = 'Task delete!'
