"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
from core.views import current_datetime, hours_ahead
from books.views import search, contact, add_publisher, add_author, add_book, book_list, author_list, publisher_list, contact_thanks
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/', current_datetime, name='current_datetime'),
    path('search/', search, name='search'),  # Added name for reverse URL lookup
    path('contact/', contact, name='contact'),  # Added name for reverse URL lookup
    path('books/add/', add_book, name='add_book'),
    path('authors/add/', add_author, name='add_author'),
    path('publishers/add/', add_publisher, name='add_publisher'),
    path('books/', book_list, name='book_list'),
    path('authors/', author_list, name='author_list'),
    path('publishers/', publisher_list, name='publisher_list'),
    path('contact/thanks/', contact_thanks, name='contact_thanks'),
    re_path(r'^time/plus/(?P<hours>[0-9]{1,2})/$', hours_ahead, name='hours_ahead'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
