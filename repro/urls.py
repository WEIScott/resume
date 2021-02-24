from django.contrib import admin
from django.urls import path, include

from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reapp.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
