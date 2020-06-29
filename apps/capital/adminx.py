import xadmin
from apps.capital.models import Capital, MoneyRecord


class CapitalAdmin(object):
    # 显示的列
    list_display = ['capital_id', 'user', "execute_id", "tasks_id", "type", "add_time"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['capital_id', 'user', "execute_id", "tasks_id", "type"]
    # 过滤
    list_filter = ['capital_id', 'user', "execute_id", "tasks_id", "type", 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(Capital, CapitalAdmin)


class MoneyRecordAdmin(object):
    # 显示的列
    list_display = ['record_id', 'user', "money", "state", "remarks", "add_time"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['record_id', 'user', "money", "state"]
    # 过滤
    list_filter = ['record_id', 'user', "money", "state", 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(MoneyRecord, MoneyRecordAdmin)

