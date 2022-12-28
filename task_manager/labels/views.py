from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from labels.forms import LabelForm
from labels.models import Label
from django.shortcuts import render


def index(request):
    labels = Label.objects.all()
    return render(request, 'labels/index.html', {'labels': labels})


class CreateLabelView(LoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels')
    success_message = 'Label create!'


class UpdateLabelView(LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels')
    success_message = 'Label update!'


class DeleteLabelView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels')
    success_message = 'Label delete!'
