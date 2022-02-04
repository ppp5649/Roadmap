from django.shortcuts import render, redirect
from user.models import BoardMember
from board.models import Post
from board.forms import BoardForm
from django.contrib.auth.decorators import login_required

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


def board_write(request):
    if not request.session.get('user'):
        return redirect('/user/login/')
    # 세션에 'user' 키를 불러올 수 없으면, 로그인하지 않은 사용자이므로 로그인 페이지로 리다이렉트 한다.

    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            # form의 모든 validators 호출 유효성 검증 수행
            user_id = request.session.get('user')
            user = BoardMember.objects.get(pk=user_id)

            post = Post()
            post.title = form.cleaned_data['title']
            post.contents = form.cleaned_data['contents']
            post.name = form.cleaned_data['name']
            # 검증에 성공한 값들은 사전타입으로 제공 (form.cleaned_data)
            # 검증에 실패시 form.error 에 오류 정보를 저장

            post.writer = user
            post.save()

            return redirect('/board/1/')

    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})
