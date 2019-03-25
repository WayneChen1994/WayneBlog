from rest_framework import viewsets

from .models import Link
from .serializers import LinkSerializer


class LinkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
