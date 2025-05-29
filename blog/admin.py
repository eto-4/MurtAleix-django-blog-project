"""
Configuració del panell d'administració de Django per al model Post, Author i Tag.

Aquest mòdul registra els models principals del blog al panell d'administració de Django,
per tal que puguin ser gestionats fàcilment a través de la interfície administrativa web.
"""

from django.contrib import admin
from .models import Post, Author, Tag

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
