from django.urls import path
from rest_framework import routers
from .views import Todos, TodoDetail

urlpatterns = [
    path('todo/', Todos.as_view()),
    path('todo/<int:id>/', TodoDetail.as_view()),
]