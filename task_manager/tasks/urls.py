from django.urls import path

from statuses.views import CreateStatusView
from users import views


urlpatterns = [
    # path('', views.users_page, name='statuses'),
    # path('create/', CreateTaskView.as_view(), name='create_status'),
    # path('<int:pk>/update/', UpdateUser.as_view(), name='update'),
    # path('<int:pk>/delete/', DeleteUser.as_view(), name='delete'),
]