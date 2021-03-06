from django.shortcuts import render
from .serializers import NoteSerializer, CategorySerializer
from .models import Note, Category
from .permissions import AdminOrReadOnly, NoteOwnerOrReadOnly, AuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView



class NoteListAV(ListCreateAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        owner = self.request.user
        return Note.objects.filter(owner=owner)


class NoteDetailAV(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [NoteOwnerOrReadOnly]



class CategoryListAV(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AuthenticatedOrReadOnly]
    

class CategoryDetailAV(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminOrReadOnly]