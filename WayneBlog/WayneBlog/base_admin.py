import re
from blog.models import Post


class BaseOwnerAdmin:
    """
    1、用来自动补充文章、分类、标签、侧边栏、友链这些Model的owner字段
    2、用来针对queryset过滤当前用户的数据
    """
    exclude = ('owner', )

    def get_list_queryset(self):
        request = self.request
        qs = super().get_list_queryset()
        if hasattr(qs.first(), 'owner'):
            qs = qs.filter(owner=request.user)
        elif hasattr(qs.first(), 'target'):
            all_comment_target = qs.values_list('target', flat=True)
            print('target: ', all_comment_target)
            # 有评论的所有文章的id集合
            all_post_ids_with_comment = set([int(re.search(r'\d+', target).group()) for target in all_comment_target])
            # 当前用户的所有文章的id集合
            current_user_post_ids = set(Post.objects.filter(status=Post.STATUS_NORMAL, owner=request.user).values_list('id', flat=True))
            # 当前用户的有评论的文章的id集合
            current_user_post_ids_with_comment = all_post_ids_with_comment & current_user_post_ids
            # 属于当前用户所发表文章的评论target集合
            targets_of_current_user_posts = set(filter(lambda target: int(re.search(r'\d+', target).group()) in current_user_post_ids_with_comment, all_comment_target))
            qs = qs.filter(target__in=targets_of_current_user_posts)
        return qs

    def save_models(self):
        self.new_obj.owner = self.request.user
        return super().save_models()
