from django import forms

# form for book detail inputs
class BookForm(forms.Form):
    title = forms.CharField(label='title', max_length=100)
    author = forms.CharField(label='author', max_length=100)
    genre = forms.CharField(label='genre', max_length=100)
    hight = forms.CharField(label='hight', max_length=100)
    publisher = forms.CharField(label='publisher', max_length=100)

#  form for search text  
class SearchForm(forms.Form):
    search = forms.CharField(label='search', max_length=100)
    select = forms.CharField(label='select', max_length=100)
    