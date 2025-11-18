from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status, permissions, viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from .models import Todo
from .serializer import TodoSerializer, TodoDetailSerializer, TodoCreateSerializer
# Create your views here.


class Todos(CreateModelMixin, ListModelMixin, GenericAPIView):
    queryset = Todo.objects.filter(complete=False)
    def get_serializer_class(self):
        # 요청 메서드에 따라 다른 시리얼라이저 반환
        if self.request.method == "GET":
            return TodoSerializer
        elif self.request.method == "POST":
            return TodoCreateSerializer
        return TodoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TodoDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Todo.objects.filter(complete=False)
    serializer_class = TodoDetailSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)