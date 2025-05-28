from django.apps import AppConfig

class BlogConfig(AppConfig):
    
    """
    Configuració principal de l'aplicació Blog.

    Aquesta classe defineix la configuració per defecte de l'app 'blog',
    incloent el nom i el tipus de clau primària per defecte per als models.
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
