from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class PostJob(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    img = models.ImageField()
    dateCreate = models.DateTimeField()
    category = TaggableManager()
    likeCount = models.IntegerField(null=True)
    viewCount = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class PostMajor(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    img = models.ImageField()
    dateCreate = models.DateTimeField()
    category = TaggableManager()
    likeCount = models.IntegerField(null=True)
    viewCount = models.IntegerField(null=True)

    def __str__(self):
        return self.title
