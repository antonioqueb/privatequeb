from rest_framework import serializers
from blog.models import Author, Category, BlogPost, PostImage, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('id', 'image')


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'post', 'name', 'email', 'content', 'date_posted', 'parent', 'replies')


class BlogPostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'content', 'category', 'image', 'date_posted', 'author', 'images', 'comments')
