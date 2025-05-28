from django.test import TestCase
from .models import Tag

class TagModelTest(TestCase):
    def setUp(self):
        """Crea un objecte Tag amb nom 'Django' per utilitzar en els tests."""
        self.tag = Tag.objects.create(name="Django")
        
    def test_tag_creation(self):
        """Comprova que el tag s'ha creat correctament amb el nom assignat."""
        self.assertEqual(self.tag.name, "Django")
        
    def test_tag_str_representation(self):
        """Comprova que la representació en cadena del tag és igual al seu nom."""
        self.assertEqual(str(self.tag), "Django")
        
    def test_tag_name_unique(self):
        """Comprova que no es poden crear dos tags amb el mateix nom (unicitat)."""
        with self.assertRaises(Exception):
            Tag.objects.create(name="Django")
