from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag

def index(request):
    """
    Vista per la pàgina d'inici.
    Mostra els 3 posts més recents.
    """
    posts = Post.objects.all()[:3]
    return render(request, 'blog/index.html', {'posts': posts})

def posts_list(request):
    """
    Vista per mostrar la llista completa de posts.
    """
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    """
    Vista per mostrar el detall d'un post identificat pel seu slug.
    """
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def authors_list(request):
    """
    Vista per mostrar la llista d'autors.
    """    
    authors = Author.objects.all()
    return render(request, 'blog/authors_list.html', {'authors': authors})

def author_detail(request, author_id):
    """
    Vista per mostrar el detall d'un autor i els seus posts.
    """
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'blog/author_detail.html', {'author': author})

def tags_list(request):
    """
    Vista per mostrar la llista d'etiquetes.
    """
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})

def tag_posts(request, tag):
    """
    Vista per mostrar els posts associats a una etiqueta concreta.
    """
    tag_obj = get_object_or_404(Tag, name=tag)
    posts = tag_obj.posts.all()
    return render(request, 'blog/tag_post.html', {'tag': tag_obj, 'posts': posts})

def custom_404(request, exception):
    """
    Vista personalitzada per l'error 404 (pàgina no trobada).
    """
    return render(request, 'blog/404.html', status=404)
