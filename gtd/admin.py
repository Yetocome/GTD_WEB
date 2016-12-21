from django.contrib import admin
from gtd.models import (
    User, ScheduleItem, TodoItem, Pomodoro, Tag,
    HealthLog, TagAndSchedule, TagAndTodo
)
# Register your models here.

admin.site.register(Pomodoro)
admin.site.register(Tag)
admin.site.register(HealthLog)
admin.site.register(TagAndSchedule)
admin.site.register(TagAndTodo)


def mark_as_done(modeladmin, request, queryset):
    queryset.update(done_flag=True)
mark_as_done.short_description = "Mark all todo as done"

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ['todo', 'due_time', 'user']
    ordering = ['done_flag']
    actions = [mark_as_done]

admin.site.register(TodoItem, TodoItemAdmin)

class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ['routine', 'start_time', 'end_time']

admin.site.register(ScheduleItem, ScheduleItemAdmin)
