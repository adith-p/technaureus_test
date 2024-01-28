from django.urls import path
from . import views

app_name = 'library_app'
urlpatterns = [
    #  list all the authors and books seperately
    path('books/',views.listAllBooks,name="listAllBooks"),
    path('authors/',views.listAllAuthors,name="listAllAuthors"),
    
    #  detail view of the author
    path('authors/<uuid:a_id>/',views.getAuthorInfo,name="getAuthorInfo"),
    
    #  create,update authors and books for each users.
    path('authors/manage/',views.manageAuthorsView,name="manageAuthorsView"),
    path('books/manage/',views.manageBooksView,name="manageBooksView"),
    
    #  Keyword searching 
    path('search/books/',views.searchBooks,name="searchBooks"),
    path('search/authors/',views.searchAuthors,name="searchAuthors"),
]
