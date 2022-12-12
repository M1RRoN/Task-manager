from django.urls import path
from users import views

urlpatterns = [
    path('', views.users_page, name='users'),
    path('create/', views.create, name='create_user'),
    # path('/<int:pk>/update/', views.update, name='update_user'),
    # path('/<int:pk>/delete', views.delete, name='delete_user'),
    path('login/', views.login, name='login'),
    # path('/logout', views.logout, name='logout'),
]
