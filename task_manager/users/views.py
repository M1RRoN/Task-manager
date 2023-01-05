from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from Mixin import MyLoginRequiredMixin, UserPermissionMixin
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
    success_message = 'User create'


class UpdateUser(SuccessMessageMixin, MyLoginRequiredMixin, UserPermissionMixin, UpdateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = 'User update'


class DeleteUser(SuccessMessageMixin, MyLoginRequiredMixin, UserPermissionMixin, DeleteView):
    model = CustomUser
    template_name = 'users/delete.html'
    success_url = reverse_lazy('login')
    success_message = 'User delete'
