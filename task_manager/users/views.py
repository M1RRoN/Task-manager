from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, UpdateView, DeleteView
from .forms import UserForm
from .models import CustomUser


def users_page(request):
    users = CustomUser.objects.all()
    return render(request, 'users/users.html', {'users': users})


class RegisterUser(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('home')
    success_message = 'User create!'


class UpdateUser(SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = 'USER_UPDATE_MESSAGE'


class DeleteUser(DeleteView):
    model = CustomUser
    template_name = 'users/delete.html'
    success_url = reverse_lazy('login')
