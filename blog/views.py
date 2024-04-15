from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from users.models import Friend
from django.contrib.auth.models import User

def home(request):
    flist = Friend.objects.filter(friend_of=request.user)
    
    context = {
        'posts' : Post.objects.all(),
        'flist' : flist,
        'suggested' : User.objects.all(),
    }
    return render(request,'blog/home.html',context)

def about(request):
    context = {
        'title' : 'About',
    }
    return render(request,'blog/about.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']