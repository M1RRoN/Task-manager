from django.urls import path
from users import views
from users.views import RegisterUser
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.users_page, name='users'),
    path('create/', RegisterUser.as_view(), name='create_user'),
    # path('<int:pk>/update/', views.update, name='update_user'),
    # path('<int:pk>/delete/', views.delete, name='delete_user'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
