from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from .forms import PostForm


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.dataPublicacao = timezone.now()
            post.save()
            return redirect('conteudo-home')

    else:
        form = PostForm()
    return render(request, 'core/new_conteudo.html', {'form':form})

