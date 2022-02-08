from django.db import models
from django.contrib.auth.models import User
from board.models import Post


class BoardMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=15, verbose_name='유저ID')
    email = models.EmailField(max_length=20, verbose_name='유저메일')
    password = models.CharField(max_length=15, verbose_name='유저PW')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='마지막수정일')
    like_posts = models.ManyToManyField(
        Post, blank=True, related_name='like_users')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'boardmembers'
        verbose_name = '게시판멤버'
        verbose_name_plural = '게시판멤버'
