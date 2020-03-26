from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('', views.home_view, name='index'),
    path('download/', views.real_download),
    path('edit/', views.song_edit_view, name='edit'),
    path('next/', views.next_page),
    # path('list/', views.list, name='list'),
    ]

