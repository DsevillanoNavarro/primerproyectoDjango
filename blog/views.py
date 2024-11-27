from django.shortcuts import render
from .models import Post
# Create your views here.
def principal(request):
    posts = Post.objects.all()
    autores = Post.objects.all().values_list('autor',flat=True).distinct()
    return render(request, 'blog/principal.html',{"posts":posts,
                                                  "autores":autores})
def menu(request):
    posts = Post.objects.all().order_by('-fecha')
    return render(request, 'blog/menu.html',{"posts":posts})