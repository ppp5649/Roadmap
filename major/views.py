from django.shortcuts import render
from main.models import PostMajor
# Create your views here.


def major(request):
    post_major = PostMajor.objects.all()
    return render(request, 'major.html', {'post_major': post_major})
