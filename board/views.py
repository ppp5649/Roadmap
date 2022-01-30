from django.shortcuts import render, redirect
from user.models import BoardMember
from board.models import Post

# Create your views here.


def job(request):
    job_models = Post.objects.filter(name='직업리뷰').order_by('-id')
    return render(request, 'board.html', {'post': job_models, 'board_name': '직업'})


def major(request):
    major_models = Post.objects.filter(name='학과리뷰').order_by('-id')
    # name이 major인 모델을 조회해서 쿼리셋으로 반환 (역순으로 노출)
    return render(request, 'board.html', {'post': major_models, 'board_name': '학과'})


def board_detail(request, pk):
    board_detail = Post.objects.get(pk=pk)
    return render(request, 'board_detail.html', {'board_detail': board_detail})
