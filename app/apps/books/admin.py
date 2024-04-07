from django.contrib import admin

from books.models import Author, Book, BookReview


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'created_at')
    list_filter = ('authors', 'created_at')
    search_fields = ('title', 'isbn', 'description')
    filter_horizontal = ('authors',)


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'stars')
    list_filter = ('stars', 'created_at')
    search_fields = ('comment', 'book__title')
