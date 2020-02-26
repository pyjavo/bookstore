from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .models import Book


class BookListView(ListView):
    """Show all books."""

    model = Book


class BookDetailView(DetailView):
    """Show the requested book."""

    model = Book
    pk_url_kwarg = "isbn"
    template_name = "books/book_detail.html"

    def get_object(self):
        return self.model.objects.get(isbn=self.kwargs['isbn'])


class BookCreateView(CreateView):
    """Create a new book."""

    model = Book
    fields = '__all__'

    # TODO: add a message on the page if form is valid: 'The book created successfully!'
    # TODO: add a message on the page if form is invalid: 'The creation has failed.'


class BookUpdateView(UpdateView):
    """Update the requested book."""

    model = Book
    fields = '__all__'
    pk_url_kwarg = "isbn"
    template_name = "books/book_form.html"

    def get_object(self):
        return self.model.objects.get(isbn=self.kwargs['isbn'])

    # TODO: add a message on the page if form is valid: 'The book updated successfully!'
    # TODO: add a message on the page if form is invalid: 'The update has failed.'


class BookDeleteView(DeleteView):
    """Delete the requested book."""

    model = Book
    pk_url_kwarg = "isbn"
    template_name = "books/book_confirm_delete.html"

    def get_object(self):
        return self.model.objects.get(isbn=self.kwargs['isbn'])

    # TODO: add a message on the page if form is valid: 'The book deleted successfully!'
    # TODO: add a message on the page if form is invalid: 'The deletion has failed.'
