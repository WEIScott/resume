from django.contrib import admin
from django.urls import path, include

from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reapp.urls')),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
