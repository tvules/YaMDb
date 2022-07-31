from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


@admin.register(Review, Comment)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text')
    list_filter = ('pub_date',)


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('year', 'genre__name', 'category__name')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
