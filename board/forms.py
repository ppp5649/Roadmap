from django.contrib.auth.hashers import check_password

from django import forms
from board.models import Post


class BoardForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'name',
            'title',
            'contents',

        ]

    name_choices = (('직업리뷰', '직업리뷰'), ('학과리뷰', '학과리뷰'))

    name = forms.ChoiceField(error_messages={
        'required': '게시판명을 선택하세요.'},
        choices=name_choices, label="게시판명")

    title = forms.CharField(error_messages={
        'required': '제목을 입력하세요.'
    }, max_length=100, label="게시글 제목")

    contents = forms.CharField(error_messages={
        'required': '내용을 입력하세요.'
    }, widget=forms.Textarea, label="게시글 내용")
