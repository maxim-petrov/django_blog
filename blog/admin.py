from django.contrib import admin

from .models import Post
from .constants import (
    POST_ADMIN_LIST_FILTER, POST_ADMIN_LIST_DISPLAY, POST_ADMIN_SEARCH_FIELDS
)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    search_fields = ('title', 'content')
    list_filter = ('title',)


admin.site.register(Post, PostAdmin)