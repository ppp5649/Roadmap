from django.contrib import admin
from main.models import PostJob, PostMajor


class PostJobAdmin(admin.ModelAdmin):
    list_display = ('title')


admin.site.register(PostJob)


class PostMajorAdmin(admin.ModelAdmin):
    list_display = ('title')


admin.site.register(PostMajor)
