from rest_framework import generics, mixins
from books.models import Book
from .serializer import  bookSerializer

class bookAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  resource_name = 'books'
  serializer_class = bookSerializer

  def get_queryset(self):
    return Book.objects.all()

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

