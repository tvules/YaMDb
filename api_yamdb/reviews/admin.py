from django.contrib import admin

from .models import Comment, Review
from users.models import User


@admin.register(Review, Comment)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text')
    list_filter = ('pub_date',)


@admin.register(User)
class userAdmin(admin.ModelAdmin):
    list_filter = ('username',)
