from django.urls import path
from todo import views

urlpatterns = [
    path('', views.todo_list, name="todo_list"),
    path('<int:pk>/', views.todo_detail, name="todo_detail"),
    path('post/', views.todo_create, name="todo_post"),
    path('<int:pk>/update/', views.todo_update, name="todo_update"),
    path('done/', views.done_list, name="done_list"),
    path('done/<int:pk>/', views.todo_done, name="todo_done")
]