from django.contrib import admin
from django.urls import path, include


api_urls = [
    path('v1/', include('apps.comics.infrastructure.dj.comicsapp.urls')),
]

urlpatterns = [
    path('api/', include(api_urls)),
    path('admin/', admin.site.urls),
]
