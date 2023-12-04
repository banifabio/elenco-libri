from django.urls import path
from . import views

# app_name = 'elencolibri'
urlpatterns = [
    path('', views.MainPage, name='mainpage'),
    path('list-page/', views.ListPage, name='listpage'),
    path('list-search/', views.ListSearch, name='search'),
    path('add-book/', views.AddBookPage, name='addbookpage'),
    path('add-list/', views.AddListPage, name='addlistpage'),
    path('export-list/', views.ExportListPage, name='exportlistpage'),
]
