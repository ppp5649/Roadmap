from django.shortcuts import render
from board.models import Post


def index(request):
    # 모든 객체를 조회해서 쿼리셋으로 반환
    job_models = Post.objects.filter(name='직업리뷰').order_by('-id')
    # job_models -> name이 '직업리뷰'인 모델을 모두 불러옴
    major_models = Post.objects.filter(name='학과리뷰').order_by('-id')
    return render(request, 'index.html', {'job_models': job_models, 'major_models': major_models})
    # index.html 안에서 job_models란 문자열로 job_models를 사용하겠다.
