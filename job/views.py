from django.shortcuts import render
from main.models import PostJob

# Create your views here.


def job(request):
    post_job = PostJob.objects.all()  # 모든 객체를 조회해서 쿼리셋으로 반환
    return render(request, 'job.html', {'post_job': post_job})

# post_job 이라는 이름으로 post_job 객체를 job.html에 전달한다.
