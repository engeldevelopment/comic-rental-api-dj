from django.urls import path

from . import views


app_name = 'comics'

urlpatterns = [
    path('comics', views.ComicListAPIView.as_view(), name='index'),
    path('comics/<int:pk>/rent/', views.rent_comic, name='rent_comic'),
]
