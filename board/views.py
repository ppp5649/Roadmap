from django.shortcuts import render
from main.models import Post

# Create your views here.


def job(request):
    job_models = Post.objects.filter(name='job').order_by('-id')
    # 모든 객체를 조회해서 쿼리셋으로 반환 (역순으로 노출)
    return render(request, 'board.html', {'post': job_models, 'board_name': '직업'})


def major(request):
    major_models = Post.objects.filter(name='major').order_by('-id')
    # 모든 객체를 조회해서 쿼리셋으로 반환 (역순으로 노출)
    return render(request, 'board.html', {'post': major_models, 'board_name': '학과'})

# post_major 이라는 이름으로 post_major 객체를 major.html에 전달한다.
