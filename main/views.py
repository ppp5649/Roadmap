from django.shortcuts import render
from main.models import Post


def index(request):
    # 모든 객체를 조회해서 쿼리셋으로 반환
    job_models = Post.objects.filter(name='job').order_by('-id')
    major_models = Post.objects.filter(name='major').order_by('-id')
    return render(request, 'index.html', {'job_models': job_models, 'major_models': major_models})
    # job_models -> name이 job인 모델을 가져온 것


def post_detail(request, pk):
    post_detail = Post.objects.get(pk=pk)
    return render(request, 'postdetail.html', {'post_detail': post_detail})
