import xadmin
from apps.news.models import News


class NewsAdmin(object):
    # 显示的列
    list_display = ['new_id', 'new_title']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['new_id', 'new_title']
    # 过滤
    list_filter = ['new_id', 'new_title', 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(News, NewsAdmin)




