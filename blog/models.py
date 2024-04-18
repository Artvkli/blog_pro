import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class Categories(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categories, related_name='articles')
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to='images/article')
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    pub_date = models.DateField(default=timezone.now())
    slug = models.SlugField(unique=True,null=True,blank=True)
    
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def __str__(self):
        return f"{self.title} - {self.body[:20]}"

    def get_absolute_url(self):
        return reverse('blog:details', kwargs={'slug': self.slug})
