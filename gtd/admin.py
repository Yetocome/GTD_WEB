from django.contrib import admin
from gtd.models import (
    User, ScheduleItem, TodoItem, Pomodoro, Tag,
    HealthLog, TagAndSchedule, TagAndTodo
)
# Register your models here.

admin.site.register(User)
admin.site.register(ScheduleItem)
admin.site.register(TodoItem)
admin.site.register(Pomodoro)
admin.site.register(Tag)
admin.site.register(HealthLog)
admin.site.register(TagAndSchedule)
admin.site.register(TagAndTodo)
