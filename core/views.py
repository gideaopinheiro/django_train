from django.shortcuts import render
from django.utils import timezone

from conteudo.models import Post

def home(request):
    conteudo = Post.objects.filter(dataPublicacao__lte=timezone.now()).order_by('dataPublicacao')

    context = {
        'conteudo':conteudo,
    }
    return render(request, 'core/conteudo.html', context)
