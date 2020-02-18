from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post, PostForm
from django.utils import timezone
from django.views.generic import ListView, FormView, UpdateView
from django.core.paginator import Paginator


class Index(ListView):
    def get(self, request, *args, **kwargs):
        posts_list = Post.objects.all().order_by('-data_publicacao')
        paginator = Paginator(posts_list, 20)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        search = request.GET.get('search')
        if search:
            posts = Post.objects.filter(nome__icontains=search)
        context = {'posts':posts}
        return render(request, 'core/index.html', context)

def index(request): 
    posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao') 
    search = request.GET.get('search')
    if search:
        posts = Post.objects.filter(subtopico__icontains=search)
    return render(request, 'core/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'core/post.html', {'post': post})

def page_topic(request, topico):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now(), topico=topico).order_by('data_publicacao')
    return render(request, 'core/index.html', {'posts':posts})

def about(request):
    return render(request, 'core/about.html')

class PageTopic(ListView):
    def get(self, request, topico, *args, **kwargs):
        posts_list = Post.objects.filter(data_publicacao__lte=timezone.now(), topico__icontains=topico).order_by('-data_publicacao')
        paginator = Paginator(posts_list, 20)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        search = request.GET.get('search')
        if search:
            posts = Post.objects.filter(subtopico__icontains=search)
        context = {'posts':posts}
        return render(request, 'core/index.html', context)

