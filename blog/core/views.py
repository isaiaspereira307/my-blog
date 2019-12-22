from django.shortcuts import render, get_object_or_404
from core.models import Post
from django.utils import timezone



from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, FormView, View
from django.http import HttpResponseRedirect
from core.models import *
from datetime import datetime
import json
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request): 
    posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao') 
    return render(request, 'core/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'core/post.html', {'post': post})

def page_topic(request, topico):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now(), topico=topico).order_by('data_publicacao')
    return render(request, 'core/index.html', {'posts':posts})

def about(request):
    return render(request, 'core/about.html')

'''
class SaoFranciscoList(ListView):
    def get(self, request, *args, **kwargs):
        posts_list = CasaSaoFrancisco.objects.all()
        paginator = Paginator(posts_list, 5)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        search = request.GET.get('search')
        if search:
            posts = CasaSaoFrancisco.objects.filter(nome__icontains=search)

        context = {'posts':posts}
        return render(request, 'core/listas/listasaofrancisco.html', context)  
'''