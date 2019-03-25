from rest_framework import viewsets, status
from rest_framework.exceptions import APIException
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Post, Category, Tag
from .serializers import (
    PostSerializer, PostDetailSerializer, CreateNewPostSerializer,
    CategorySerializer, CategoryDetailSerializer,
    TagSerializer, TagDetailSerializer,
)


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """ 提供文章接口 """
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.filter(status=Tag.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = TagDetailSerializer
        return super().retrieve(request, *args, **kwargs)


class MyAPIException(APIException):
    status_code = status.HTTP_200_OK


class CreateNewPostViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = CreateNewPostSerializer

    def http_method_not_allowed(self, request, *args, **kwargs):
        raise MyAPIException(request.method)
