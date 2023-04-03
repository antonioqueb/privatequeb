from django.db import models
from datetime import datetime
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=50, default="Antonio Queb")
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='author_profiles', default='default.jpg')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, default="Category Name")

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200, default="Post Title")
    content = models.TextField(default="Post Content")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', default=1)
    image = models.ImageField(upload_to='post_images', default='default.jpg')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts', default=1)

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images', default='default.jpg')

    def __str__(self):
        return f'{self.post.title} - Image'

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments', null=True)
    name = models.CharField(max_length=50, default="Commenter Name")
    email = models.EmailField(default="commenter@example.com")
    content = models.TextField(default="Comment Content")
    date_posted = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f'{self.name} - {self.post.title}'
