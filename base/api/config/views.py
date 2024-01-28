from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from library_app.models import Book,Author

from .serializers import BookSerializer,AuthorSerializer

class List_books_view(APIView):
    
    def get_queryset(self,query=None):
        if query:
            book_list=Book.search(query)
        else:
            book_list=Book.objects.all()
        return book_list
    
    @swagger_auto_schema(
        
        responses={200: BookSerializer},
        tags=["Books"],
        manual_parameters=[
            openapi.Parameter(
                name="q",
                in_=openapi.IN_QUERY,
                description="Search query",
                type=openapi.TYPE_STRING,
            ),
        ]
    )    
    def get(self,request):
        query = request.query_params.get('q', '')
        book_list=self.get_queryset(query)
        serializer=BookSerializer(book_list,many=True)
        return Response(serializer.data)
        

    
class List_author_view(APIView):
    
    def get_queryset(self,query=None):
        if query:
            book_list=Author.search(query)
        else:
            book_list=Author.objects.all()
        return book_list
    
    
    @swagger_auto_schema(
        responses={200: AuthorSerializer},
        tags=["Authors"],
        manual_parameters=[
            openapi.Parameter(
                name="q",
                in_=openapi.IN_QUERY,
                description="Search query",
                type=openapi.TYPE_STRING,
            ),
        ]

    )
    def get(self,request):
        query = request.query_params.get('q', '')
        book_list=self.get_queryset(query)
        serializer=AuthorSerializer(book_list,many=True)
        return Response(serializer.data)