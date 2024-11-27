from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
    return HttpResponse("Welcome to my book store.")


#Example of function based views in django!

def hello_view(request):
    """A basic function view returning a greeting message"""
    return HttpResponse("Hello, World!")

def book_list(request):
    """Retrieving all books and renders a template displaying the list."""
    books = Book.objects.all() #Fetch all book instances from the database.
    context = {'book_list':books} #Create a context dictionary with book list
    return render(request, 'books/book_list.html', context)


#example of class based views in django!
from django.views.generic import TemplateView
class HelloView(TemplateView):
    """A class-based view rendering a template named 'hello.html'."""
    template_name = 'hello.html'


#Example 2;
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy


class BookDetailView(DetailView):
    """A class-based view for displaying details of a specific book."""
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the book."""
        context = super().get_context_data(**kwargs) #Get default context data
        book = self.get_object() #Retrieve the current book instance
        context['average_rating'] = book.get_average_rating()


#Example 3;

class BookUpdateView(UpdateView):
    """A class-based view for updating details of a specific book."""
    model = Book
    felds = ['title','author','description'] #Specify fields to be editable
    template_name = 'books/book_update_form.html'
    success_url = reverse_lazy('book_list') # URL to redirect after successful update

    def form_valid(self, form):
        """Executes custom logic after form validation."""
        response = super().form_valid(form) # Call default form validation
        # Perform additional actions after successful update(e.g., send notifications)
        return response