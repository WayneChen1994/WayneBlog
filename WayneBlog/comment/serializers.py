from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api-comment-detail')
    target = serializers.SerializerMethodField('get_full_url')

    def get_full_url(self, obj):
        raw_req = self.context['request']._request
        host = raw_req.scheme + '://' + raw_req.get_host()
        return host + obj.target

    class Meta:
        model = Comment
        fields = (
            'url', 'id', 'target', 'nickname', 'website', 'email', 'created_time',
        )


class CommentDetailSerializer(CommentSerializer):
    class Meta:
        model = Comment
        fields = (
            'id', 'target', 'nickname', 'website', 'email', 'created_time', 'content',
        )
