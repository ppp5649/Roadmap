"""roadmap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import index, post_job_detail, post_major_detail
from job.views import job
from major.views import major
from django.conf.urls.static import static
from django.conf import settings
from user.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('job/', job, name='job'),
    path('major/', major, name='major'),
    path('postjob/<int:pk>', post_job_detail, name='jobdetail'),
    path('postmajor/<int:pk>', post_major_detail, name='majordetail'),
    path('user/', include('user.urls')),
    path('', home, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
