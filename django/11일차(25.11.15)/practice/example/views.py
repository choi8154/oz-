from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions, viewsets
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from .models import Books
from .serializers import BookSerializer



@api_view(['GET', 'POST'])
def booksAPI(request):
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BookSerializer(instance=books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def bookAPI(request, bid):
    book = get_object_or_404(Books, bid=bid)
    serializer = BookSerializer(instance=book)
    return Response(serializer.data, status=status.HTTP_200_OK)



class BooksAPI(APIView):
    def get(self, reqeust):
        books = Books.objects.all()
        serializer = BookSerializer(instance=books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Books, bid=bid)
        serializer = BookSerializer(instance = book)
        return Response(serializer.data, status=status.HTTP_200_OK)



class BooksMixins(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class BookMixin(RetrieveModelMixin, GenericAPIView, UpdateModelMixin, DestroyModelMixin):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer