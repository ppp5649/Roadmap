from django.contrib.auth.hashers import check_password

from django import forms
from importlib_metadata import email
from .models import BoardMember


class LoginForm(forms.Form):
    # 입력받을 값 두개
    email = forms.EmailField(error_messages={
        'required': '이메일을 입력하세요!'
    }, max_length=100, label="이메일")
    password = forms.CharField(error_messages={
        'required': '비밀번호를 입력하세요!'
    }, widget=forms.PasswordInput, max_length=100, label="비밀번호")
    # 처음 값이 들어왔다 는 검증 진행

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = BoardMember.objects.get(email=email)

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 다릅니다!')
            else:
                self.user_id = user.id
