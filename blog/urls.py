from django.urls import path, include
from .views import PostListView
from . import views
urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('about/',views.about,name='blog-about'),
]