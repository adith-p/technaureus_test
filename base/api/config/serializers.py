from rest_framework import serializers

from library_app.models import Book,Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
        
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True, many=True)
    class Meta:
        model=Author
        fields=('author_id','author_name','username','email_id','books')