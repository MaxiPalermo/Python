from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})
def buscar(request):
    titulo = request.GET.get("titulo", "")
    posts = Post.objects.filter(titulo__icontains=titulo)
    return render(request, "buscar.html", {"posts": posts})
