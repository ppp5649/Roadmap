from django.db import models
from user.models import BoardMember


# 게시판 관련 모델
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    img = models.ImageField(verbose_name="이미지")
    writer = models.ForeignKey(
        BoardMember, on_delete=models.CASCADE, null=True, verbose_name="작성자")
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="작성일")
    updated_at = models.DateTimeField(
        auto_now=True, null=True, verbose_name="최종수정일")
    view_count = models.PositiveIntegerField(default=0, verbose_name="조회수")
    like_count = models.PositiveIntegerField(default=0, verbose_name="좋아요수")
    # User 와 M:M 관계
    name_choices = (('직업리뷰', '직업리뷰'), ('학과리뷰', '학과리뷰'))
    name = models.CharField(
        max_length=200, null=True, choices=name_choices, verbose_name="게시판명")
    # choiceField는 존재하지않음 튜플 형태로 charField에 넣어주는 형태로 만들 수 있음

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'boards'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'
