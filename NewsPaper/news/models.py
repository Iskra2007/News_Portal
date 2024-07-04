from datetime import datetime
from django.db import models
from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    bio = models.TextField(default="Информация об авторе")


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="Описание категории")


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    publication_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def finish_publication(self):
        self.publication_date = datetime.now()
        self.is_published = True
        self.save()

    def get_prescription(self):
        return (datetime.now() - self.publication_date).days
