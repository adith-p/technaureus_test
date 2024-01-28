from django.db import models
import uuid


# Create your models here.


class Author(models.Model):
    author_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author_name = models.CharField(max_length=120)
    username = models.CharField(max_length=120,unique=True)
    email_id = models.EmailField(max_length=120,unique=True)

    
    def __str__(self):
        return self.author_name
    
    def search (query):
        return Author.objects.filter( models.Q(author_name__icontains=query) |
        models.Q(username__icontains=query) 
        )
        
class Book(models.Model):
    book_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    book_name = models.CharField(max_length=120)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    published_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.book_name
    
    
    def search(query):
        return Book.objects.filter(
            models.Q(author__author_name__icontains=query) |
            models.Q(book_name__icontains=query)
        )

        