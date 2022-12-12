from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserForm
from .models import User

# from rest_framework.viewsets import ModelViewSet
#
# from users.models import User
# from users.serializers import UsersSerializer


# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UsersSerializer


def users_page(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def create(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Учетная запись создана!")
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    messages.warning(request, 'Неверные данные')
    return render(request, 'create.html', context)


def login(request):
    return render(request, 'login.html')
