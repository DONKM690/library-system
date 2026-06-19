from django.urls import path
from .views import *

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<int:id>/', book_details, name='book_detail'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:id>/', edit_book, name='edit_book'),
    path('delete/<int:id>/', delete_book, name='delete_book'),
]