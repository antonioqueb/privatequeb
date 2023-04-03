from django.contrib import admin
from blog.models import Author, Category, BlogPost, PostImage, Comment

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(PostImage)
admin.site.register(Comment)
