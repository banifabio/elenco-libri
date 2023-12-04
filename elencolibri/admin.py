from django.contrib import admin
from .models import Author, Topic, Bookshelf, Book

admin.site.register(Author)
admin.site.register(Topic)
admin.site.register(Bookshelf)
admin.site.register(Book)
