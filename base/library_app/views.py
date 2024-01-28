from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db import IntegrityError

from django.contrib.auth.decorators import login_required,permission_required

import uuid

from . import models,forms
# Create your views here.
@login_required(login_url='user_auth:login_user')
def listAllBooks(request):
    """
    Display a paginated list of books, ordered by published date.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered HTML page with paginated book list.
    """
    book_list = models.Book.objects.all()

    # Add ordering to show newest books first
    book_list = book_list.order_by('-published_date')
    
    total_books = book_list.count()
    total_authors = models.Author.objects.all().count()

    # Use Django's built-in pagination instead of doing it manually
    paginator = Paginator(book_list, 15) 

    page_no = request.GET.get("page")
    page_obj = paginator.get_page(page_no)

    
    context = {
        'data': page_obj,
        'total_books': total_books,
        'total_authors': total_authors
    }

    return render(request, "library_app/books_table.html", context)


@login_required(login_url='user_auth:login_user')
def listAllAuthors(request):


    author_list = models.Author.objects.all()
    total_authors = author_list.count()
    total_books = models.Book.objects.all().count()

    # Paginate authors
    paginator = Paginator(author_list, 15)
    page_no = request.GET.get("page")
    page_obj = paginator.get_page(page_no)

    author_list = author_list.order_by('author_name')

    context = {
        'data': page_obj,
        'total_books': total_books,
        'total_authors': total_authors
    }

    return render(request, "library_app/author_table.html", context)

    
@login_required(login_url='user_auth:login_user')
def getAuthorInfo(request, a_id: uuid.UUID):

    try:
        author_info = models.Author.objects.get(author_id=a_id)
    except models.Author.DoesNotExist:
        
        messages.add_message(request, messages.ERROR, "Author does not exist")
        return redirect('library_app:getAuthorInfo')

    book_info = author_info.books.all()

    # Order books by publication date
    book_info = book_info.order_by('-published_date')

    context = {
        'author_info': author_info,
        'book_info': book_info
    }
    
    return render(request, "library_app/author_details.html", context)


@login_required(login_url='user_auth:login_user')
def manageAuthorsView(request):
    """
    View to handle both creation and update of authors.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Response indicating success or failure.
    """
    
    if request.method == "POST":
        a_id = request.POST.get("idInput")
        form = forms.CreateAuthor(request.POST)

        if form.is_valid():
            
            # Get cleaned data
            author_name = form.cleaned_data['author_name']
            username = form.cleaned_data['username']
            email_id = form.cleaned_data['email_id']
            
        
            # If author id is passed, update the author
            if a_id:
                try:
                    author = models.Author.objects.get(pk=a_id)
                except models.Author.DoesNotExist:
                    messages.add_message(request, messages.ERROR, "Author does not exist")
                    return redirect('library_app:getAuthorInfo', a_id=a_id)
            else:
                author = models.Author()
            try:
                author.author_name = author_name
                author.username = username
                author.email_id = email_id
                author.save()
                messages.add_message(request, messages.SUCCESS, "Author added successfully")
                return redirect("library_app:listAllAuthors")
            except IntegrityError:
                messages.add_message(request, messages.ERROR, "Username or email ID already taken by another user")
                return redirect("library_app:listAllAuthors")
        
        # Add error message if form invalid
        messages.add_message(request, messages.ERROR, "Form validation failed")
        return redirect('library_app:getAuthorInfo', a_id=a_id)


    
    
@login_required(login_url='user_auth:login_user')
def manageBooksView(request):
    """
    View to handle both creation and update of books.

    Args:
        request: The HTTP request object.
        b_id: Optional UUID for the book to update. If not provided, creates a new book.

    Returns:
        HttpResponse: Response indicating success or failure.
    """
    if request.method == "POST":
        b_id = request.POST.get("idInput")
        form = forms.CreateBook(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data['book_name']
            author_name = form.cleaned_data['author_name']
            
            try:
                author = models.Author.objects.get(author_name=author_name)
            except models.Author.DoesNotExist:
                messages.add_message(request, messages.ERROR, "Author does not exist")
                return redirect('library_app:manageBooksView')
            
            if b_id:
                try:
                    book_obj = models.Book.objects.get(pk=b_id)
                except models.Book.DoesNotExist:
                    messages.add_message(request, messages.ERROR, "Book does not exist")
                    return redirect('library_app:manageBooksView')
            else:
                book_obj = models.Book()
                
            book_obj.book_name = book_name
            book_obj.author = author
            book_obj.save()
            return redirect("library_app:listAllBooks")
    
        messages.add_message(request, messages.ERROR, "Form validation failed")
        return redirect('library_app:getAuthorInfo')
    return redirect('library_app:listAllBooks') 



                
@login_required(login_url='user_auth:login_user')
def searchBooks(request):
    if request.method == "GET":
        query = request.GET.get("query")
        
        if query:      
            book_obj = models.Book.search(query)
            print(book_obj)
            paginator = Paginator(book_obj,15)
            
            page_no = request.GET.get('page')
            page_obj = paginator.get_page(page_no)
            
            return render(request,  "library_app/books_table.html", {"data": page_obj})
        return redirect("library_app:listAllBooks")
    
@login_required(login_url='user_auth:login_user')    
def searchAuthors(request):
    if request.method == "GET":
        query = request.GET.get("query")
        if query:      
            book_obj = models.Author.search(query)
            paginator = Paginator(book_obj,15)
            
            page_no = request.GET.get('page')
            page_obj = paginator.get_page(page_no)
            return render(request, "library_app/author_details.html", {"data": page_obj})
        return redirect("library_app:listAllAuthors")