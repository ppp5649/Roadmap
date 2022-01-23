from django.contrib import admin
from main.models import PostJob, PostMajor

admin.site.register(PostJob)
admin.site.register(PostMajor)


class PostJobAdmin(admin.ModelAdmin):
    list_display = ('title')
