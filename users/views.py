from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from task_manager.Mixin import MyLoginRequiredMixin, UserPermissionMixin
from .forms import UserForm
from .models import CustomUser


class UserList(ListView):
    model = get_user_model()
    template_name = "users/users.html"
    context_object_name = "users"


class RegisterUser(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно зарегистрирован'


class UpdateUser(UserPermissionMixin, MyLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = 'Пользователь успешно изменён'


class DeleteUser(UserPermissionMixin, MyLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CustomUser
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = 'Пользователь успешно удалён'
