from django.urls import include, path, re_path

from . import views

app_name = 'books'

urlpatterns = [
    path('',
        view=views.BookListView.as_view(),
        name='index'),
    path('create/',
        view=views.BookCreateView.as_view(),
        name='create'),
    path('<str:isbn>/',
        view=views.BookDetailView.as_view(),
        name='detail'),
    path('update/<str:isbn>/',
        view=views.BookUpdateView.as_view(),
        name='update'),
    re_path(r'^delete/(?P<isbn>[\d\-]+)/$',
        view=views.BookDeleteView.as_view(),
        name='delete'),
]
