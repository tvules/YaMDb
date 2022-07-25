from django.contrib import admin
from .models import Review, Comment


@admin.register(Review, Comment)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text')
    list_filter = ('pub_date',)
