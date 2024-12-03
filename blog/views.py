from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Autor
# Create your views here.
def principal(request):
    posts = Post.objects.all()
    return render(request, 'blog/principal.html',{"posts":posts})
def menu(request):
    posts = Post.objects.all().order_by('-fecha')
    return render(request, 'blog/menu.html',{"posts":posts})
def detalle_post(request,pk):
    context = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/detalle_post.html',{'post':context})

def autores(request):
    context = Post.objects.all()
    return render(request, 'blog/autores.html',{"posts":context})

def detalle_autor(request,pk):
    autor = get_object_or_404 (Autor, pk=pk)
    posts_autor = Post.objects.filter(autor=pk)
    
    return render(request, 'blog/detalle_autor.html',{'autor':autor,
                                                      'posts_autor': posts_autor})