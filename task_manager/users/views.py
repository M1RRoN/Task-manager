from django.shortcuts import render
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
    return render(request, 'users.html', {'title': 'Пользователи', 'users': users})

