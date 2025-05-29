"""
Definició de les rutes URL per a l'aplicació de blog.

Aquest mòdul assigna les rutes del projecte a les vistes corresponents definides al fitxer views.py.
Inclou rutes per llista de posts, detall de posts, autors i etiquetes.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/', views.posts_list, name='posts-list'),
    path('posts/<slug:slug>', views.post_detail, name='posts-detail-page'),
    path('authors/', views.authors_list, name='authors-list'),
    path('authors/<int:author_id>', views.author_detail, name='author-detail'),
    path('tags/', views.tags_list, name='tags-list'),
    path('tags/<str:tag>', views.tag_posts, name='tag-posts'),
]
