from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import gettext_lazy as _
from task_manager.dataclasses import FlashMessages
from .forms import UserForm
# from .models import CustomUser
from users import forms
# from users.forms import UserLoginForm


def users_page(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Учетная запись создана!")
#             return redirect('home')
#         else:
#             error = 'Форма была неверной'
#     form = UserForm()
#     context = {
#         'form': form,
#         'error': error
#     }
#     messages.warning(request, 'Неверные данные')
#     return render(request, 'create.html', context)

# @csrf_exempt
# def login_user(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         redirect('home')


# @login_required(login_url='/users/login/')
# def logout_user(request):
#     logout(request)
#
# @login_required(login_url='/users/login/')
# def update():
#     pass
#
# @login_required(login_url='/users/login/')
# def delete():
#     pass


class RegisterUser(CreateView):

    form_class = UserForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')


from django.views.generic import View


# class LoginPageView(View):
#     template_name = 'authentication/login.html'
#     form_class = forms.LoginForm
#
#     def get(self, request):
#         form = self.form_class()
#         message = ''
#         return render(request, self.template_name, context={'form': form, 'message': message})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         message = 'Login failed!'
#         return render(request, self.template_name, context={'form': form, 'message': message})
