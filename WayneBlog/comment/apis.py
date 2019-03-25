from rest_framework import viewsets

from .serializers import CommentSerializer, CommentDetailSerializer
from .models import Comment


class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(status=Comment.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CommentDetailSerializer
        return super().retrieve(request, *args, **kwargs)
