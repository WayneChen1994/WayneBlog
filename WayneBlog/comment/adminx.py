import xadmin

from .models import Comment
from WayneBlog.base_admin import BaseOwnerAdmin


@xadmin.sites.register(Comment)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
