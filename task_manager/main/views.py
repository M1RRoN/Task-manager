from django.shortcuts import render, redirect
# from users.forms import UserForm


def index(request):
    return render(request, 'task_manager/index.html')
