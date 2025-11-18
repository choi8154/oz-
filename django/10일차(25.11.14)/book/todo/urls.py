from django.urls import path

from todo import views

urlpatterns = [
    path('todo/', views.TodoAPIView.as_view()),
    path('todo/<int:pk>/', views.TodoDetail.as_view()),
    path('done/', views.DoneTodosAPIView.as_view()),
    path('done/<int:pk>/', views.DoneTodoAPIView.as_view())
]