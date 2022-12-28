from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from statuses.forms import StatusForm
from statuses.models import Status

from django.shortcuts import render


def index(request):
    statuses = Status.objects.all()
    return render(request, 'statuses/index.html', {'statuses': statuses})


class CreateStatusView(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')
    success_message = 'Status create!'


class UpdateStatusView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses')
    success_message = 'Status update!'


class DeleteStatusView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = 'Status delete!'
