from django.urls import path
from . import views 

urlpatterns = [
    # url for all notes and individual notes
    path('notes/', views.NoteListAV.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteDetailAV.as_view(), name='note-detail'),
    
    # url for all the categories and each categories
    path('categories/', views.CategoryListAV.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailAV.as_view(), name='category-detail')
]
