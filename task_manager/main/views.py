from django.shortcuts import render, redirect
from users.forms import UserForm


def index(request):
    return render(request, 'index.html')


def registration(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'registration.html', context)


def sign_in(request):
    return render(request, 'sign_in.html')
