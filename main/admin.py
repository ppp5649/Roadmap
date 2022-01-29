from django.contrib import admin
from main.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title')


admin.site.register(Post)
