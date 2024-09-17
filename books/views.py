from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from django.core.mail import send_mail
from rest_framework import generics
from books.models import Book
# from books.forms import ContactForm
from books.forms import PublisherForm, AuthorForm, BookForm, ContactForm
from books.models import Book, Author, Publisher
from books.serializers import BookSerializer, AuthorSerializer, PublisherSerializer

def search(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()

    # Use render instead of render_to_response
    return render(request, "search.html", {
        "results": results,
        "query": query
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender', 'noreply@example.com')  # Use get() with default fallback
            send_mail(
                f'Feedback from your site, topic: {topic}',  # Use f-string for formatting
                message,
                sender,
                ['medin0407@gmail.com'],
                fail_silently=False,  # Optional: Ensure you're notified of send_mail errors
            )
            return HttpResponseRedirect(reverse('contact_thanks'))  # Use reverse for better URL handling
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')  # Change as per your URL names
    else:
        form = PublisherForm()

    return render(request, 'contact/add_publisher.html', {'form': form})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('author_list')  # Change as per your URL names
    else:
        form = AuthorForm()

    return render(request, 'contact/add_author.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)  # Include request.FILES for image upload
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Replace with your redirect URL
    else:
        form = BookForm()

    return render(request, 'contact/add_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'contact/book_list.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'contact/author_list.html', {'authors': authors})

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'contact/publisher_list.html', {'publishers': publishers})

def contact_thanks(request):
    return render(request, 'contact/thanks.html')

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublisherListCreateView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


# Create your views here.
