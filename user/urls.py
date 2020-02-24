from django.urls import path
from . import views

# Namespacing URL names
# usage : {% url 'polls:detail' question.id %}
app_name = 'user'

urlpatterns = [
    path('', views.handle_login, name='handle_login'),
    path('list/', views.UserListView.as_view()),
]