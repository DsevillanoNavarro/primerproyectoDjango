from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Autor
from blog.forms import post_form, post_form_model, form_autores_model

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
def ji(request):
    if request.method == "POST":
        nombre = request.POST['nombre1']
        #Post.objects.create()
        print(nombre)
        print(request.POST)
        return render (request,'blog/ji.html')
    else:
        return render (request,'blog/ji.html')
def post_new(request):
    if request.method == 'POST':
        form = post_form_model(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'blog/post_added.html') 
    else:
        form = post_form()
    return render(request, 'blog/post_new.html', {"form":form})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = post_form_model(request.POST)
        if form.is_valid():
            # post.titulo= form.cleaned_data['titulo']
            # post.cuerpo = form.cleaned_data['cuerpo']
            # post.fecha = form.cleaned_data['fpublicado']
            # post.save()
            form.save()
            return render(request,'blog/post_added.html')
    else:
        form = post_form_model(initial=post.__dict__)
    
    return render(request, 'blog/post_edit.html',{"form":form})
def autores(request):
    autores = Autor.objects.all()
    return render(request, 'blog/autores.html',{"autores":autores})
def detalle_autores(request,pk):
    autor = get_object_or_404(Autor,pk=pk)
    return render(request, 'blog/autores_detalle.html',{"autor":autor})

def edit_autores(request,pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = form_autores_model(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return render(request,'blog/autor_edited.html')
    else:
        form = form_autores_model(instance=autor)
    return render(request, 'blog/autor_edit.html',{"form":form,"pk":pk})

def autores_new(request):
    if request.method == 'POST':
        form = form_autores_model(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'blog/autor_added.html')
    else:
        form = form_autores_model()
    return render(request, 'blog/autor_new.html',{"form":form})

def delete_autores(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return render(request,'blog/autores_deleted.html')
    else:
        form = form_autores_model(instance=autor)
        
    return render(request, 'blog/autor_delete_confirm.html',{"form":form,"autor":autor})
