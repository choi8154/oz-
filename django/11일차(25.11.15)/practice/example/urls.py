from django.urls import path
from .views import booksAPI, bookAPI, BookAPI, BooksAPI, BookMixin, BooksMixins, BooksViewSet

urlpatterns = [
    path('fbv/books/', booksAPI),
    path('fbv/books/<int:bid>/', bookAPI),
    path('cbv/books/', BooksAPI.as_view()),
    path('cbv/books/<int:bid>/', BookAPI.as_view()),
    path('mixin/books/', BooksMixins.as_view()),
    path('mixin/books/<int:bid>', BookMixin.as_view()),
]

from rest_framework import routers

router = routers.SimpleRouter()
router.register('books', BooksViewSet)

urlpatterns = router.urls