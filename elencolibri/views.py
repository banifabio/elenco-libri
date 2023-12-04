from django.shortcuts import render
from .forms import SearchForm
from .models import Book


def MainPage(request):
    """
    Print the main menu.
    """
    return render(request, 'home.html')


def ListPage(request):
    """
    Page to search the book list.
    """
    search_form = SearchForm()
    context = {}
    context['search_form'] = search_form
    return render(request, 'listpage.html', context)


def ListSearch(request):
    print('list search')
    if request.method == 'POST':
        context = {}
        research_key = request.POST
        title = request.POST.get('title')
        author = request.POST.get('author')
        topic = request.POST.get('topic')
        bookshelf = request.POST.get('bookshelf')
        vote = request.POST.get('vote')
        support = request.POST.get('support')
        results = Book.objects.all()
        if title:
            results = results.filter(title=title)
        if author:
            results = results.filter(author__id=author)
        if topic:
            results = results.filter(topic__id=topic)
        if bookshelf:
            results = results.filter(bookshelf__id=bookshelf)
        print('research_key', research_key)
        if not results:
            results = ['Non ci sono risultati per questa ricerca']
        context['results'] = results
    return render(request, 'resultpage.html', context)


def AddBookPage(request):
    pass


def AddListPage(request):
    pass


def ExportListPage(request):
    pass
