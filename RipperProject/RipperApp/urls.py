from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('detail/', views.link_detail_view),
    path('create/', views.link_create_view)
]