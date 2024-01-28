from django import forms

class CreateAuthor(forms.Form):
    author_name = forms.CharField(max_length=120)
    username = forms.CharField(max_length=120)
    email_id = forms.EmailField(max_length=120)
    
class CreateBook(forms.Form):
    book_name = forms.CharField(max_length=120)
    author_name = forms.CharField(max_length=120)
    
    