from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('title', 'created_date')


admin.site.register(Post, PostAdmin)