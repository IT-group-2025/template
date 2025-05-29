from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'id')
    list_filter = ('pub_date',)
    search_fields = ('title', 'content')
    date_hierarchy = 'pub_date'

