from django.urls import path

from . import views


app_name = 'comics'

urlpatterns = [
    path('comics', views.ComicListAPIView.as_view(), name='index'),
    path('comics/<int:pk>/rent/', views.ComicRentAPIView.as_view(), name='rent_comic'),
    path('rentals', views.RentalListAPIView.as_view(), name='rentals'),
]
