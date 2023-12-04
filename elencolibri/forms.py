from django import forms
from .models import Book


class SearchForm(forms.ModelForm):
    """
    Form to search the list. It gives a list of result
    """

    class Meta:
        model = Book
        fields = ['title', 'author', 'topic', 'bookshelf', 'vote', 'support']

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False
        self.fields['author'].required = False
        self.fields['topic'].required = False
        self.fields['bookshelf'].required = False
        self.fields['vote'].required = False
        self.fields['support'].required = False
