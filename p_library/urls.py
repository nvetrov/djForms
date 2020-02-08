from django.contrib import admin
from django.urls import path
from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, FriendList

app_name = 'p_library'

urlpatterns = [
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('friends', FriendList.as_view(), name='friend_add'),
    path('', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
]


# http://127.0.0.1:8000/friends
# http://127.0.0.1:8000/author/create
# http://127.0.0.1:8000/authors

