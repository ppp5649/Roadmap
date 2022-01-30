from django.contrib import admin
from board.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'writer', 'created_at', 'updated_at')


admin.site.register(Post, PostAdmin)
