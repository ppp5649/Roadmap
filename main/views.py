from django.shortcuts import render
from main.models import PostJob, PostMajor


def index(request):
    post_job = PostJob.objects.all()  # 모든 객체를 조회해서 쿼리셋으로 반환
    post_major = PostMajor.objects.all()
    return render(request, 'index.html', {'post_job': post_job, 'post_major': post_major})


def post_job_detail(request, pk):
    post_job_detail = PostJob.objects.get(pk=pk)
    # 특정 칼럼 조건에 해당하는 모델 객체를 반환 (pk : primary key)
    return render(request, 'postjobdetail.html', {'post_job_detail': post_job_detail})


def post_major_detail(request, pk):
    post_major_detail = PostMajor.objects.get(pk=pk)
    return render(request, 'postmajordetail.html', {'post_major_detail': post_major_detail})
