import xadmin
from apps.tasks.models import Tasks, CompleteTasks, Banner, TasksType


class TasksTypeAdmin(object):
    # 显示的列
    list_display = ['type', "price", "complete_price"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['type']
    # 过滤
    list_filter = ['type_id', 'type']
    ordering = ('-add_time',)


xadmin.site.register(TasksType, TasksTypeAdmin)


class TasksAdmin(object):
    # 显示的列
    list_display = ['tasks_id', 'url', "target_times", "completed_times", "tasks_name", "cost", "total_cost", "state",
                    "type", "created", "add_time"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['tasks_id', 'state', 'created', 'completed_times', 'type']
    # 过滤
    list_filter = ['tasks_id', 'state', 'created', 'completed_times', 'type', 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(Tasks, TasksAdmin)


class CompleteTasksAdmin(object):
    # 显示的列
    list_display = ['execute_id', 'tasks_id', "complete_user", "state", "remarks", "add_time"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['execute_id', 'tasks_id', "complete_user", "state"]
    # 过滤
    list_filter = ['execute_id', 'tasks_id', "complete_user", "state", 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(CompleteTasks, CompleteTasksAdmin)


class BannerAdmin(object):
    # 显示的列
    list_display = ['image', 'index', "add_time"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['image', 'index']
    # 过滤
    list_filter = ['image', 'index', 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(Banner, BannerAdmin)

