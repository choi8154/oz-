from django.urls import path, include
from example import views

urlpatterns = [
    path("hello/", views.HelloAPI),
    path("fbv/books/", views.booksAPI),
    path("fbv/books/<int:bid>", views.bookAPI),
    path("cbv/books/", views.BooksAPI.as_view()),
    path("cbv/books/<int:bid>", views.BookAPI.as_view()),
    path("mixin/books/", views.BooksAPIMixins.as_view()),
    path("mixin/book/<int:bid>/", views.BookAPIMixins.as_view()),
    path("generic/books/", views.BooksAPIGenerics.as_view()),
    path("generic/books/<int:bid>/", views.BookAPIGenerics.as_view()),
]

from rest_framework import routers
from .views import BookViewSet

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls