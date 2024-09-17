from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# from books.models import Book
from books.models import Publisher, Author, Book

# Customize the default AdminSite settings
admin.site.site_header = _("Sagacitas Technologies Admin")
admin.site.site_title = _("Sagacitas Technologies Portal")
admin.site.index_title = _("Welcome to Sagacitas Technologies Pvt Ltd.")

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'publisher', 'publication_date')
#     list_filter = ('publisher', 'publication_date')
#     search_fields = ('title',)
#     ordering = ('-publication_date',)

# admin.site.register(Book, BookAdmin)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')
    search_fields = ('name', 'city', 'country')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
    list_filter = ('last_name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    search_fields = ('title',)
    list_filter = ('publisher', 'publication_date')
    filter_horizontal = ('authors',)  # For better UI with ManyToMany fields