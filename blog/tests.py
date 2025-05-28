from django.test import TestCase
from .models import Tag

class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Django")
    def test_tag_creation(self):
        self.assertEqual(self.tag.name, "Django")
    def test_tag_str_representation(self):
        self.assertEqual(str(self.tag), "Django")
    def test_tag_name_unique(self):
        with self.assertRaises(Exception):
            Tag.objects.create(name="Django")
