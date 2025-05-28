from django.db import models

class Tag(models.Model):
    """
    Model que representa una etiqueta per classificar els posts.

    Camps:
        name (str): Nom únic de l'etiqueta.
    """
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        """Retorna el nom de l'etiqueta com a representació en text."""
        return self.name

class Author(models.Model):
    """
    Model que representa un autor que pot escriure posts al blog.

    Camps:
        first_name (str): Nom de l'autor.
        last_name (str): Cognom de l'autor.
        email (Email): Correu electrònic únic.
        bio (Text): Biografia opcional de l'autor.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    def full_name(self):
        """Retorna el nom complet de l'autor."""
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        """Retorna el nom complet com a representació en text."""
        return self.full_name()

class Post(models.Model):
    """
    Model que representa una entrada (post) del blog.

    Camps:
        title (str): Títol del post.
        slug (Slug): Slug únic per a la URL.
        content (Text): Contingut complet del post.
        excerpt (str): Resum del contingut.
        date (DateTime): Data de publicació (es genera automàticament).
        author (Author): Autor que ha escrit el post.
        tags (Tag): Etiquetes associades al post.
        image (Image): Imatge opcional per al post.

    Meta:
        ordering: Ordena els posts del més nou al més antic.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    class Meta:
        ordering = ['-date']
    def __str__(self):
        """Retorna el títol del post com a representació en text."""
        return self.title
