from django.urls import path, include
from rest_framework import routers
from blog.api.views import AuthorViewSet, CategoryViewSet, BlogPostViewSet, PostImageViewSet, CommentViewSet

router = routers.DefaultRouter()

router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'posts', BlogPostViewSet)
router.register(r'post-images', PostImageViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
