from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    work_time = models.IntegerField(default=25)
    short_break_time = models.IntegerField(default=5)
    long_break_time = models.IntegerField(default=15)
    how_many_a_break = models.IntegerField(default=4)

    def __str__(self):
        return self.name

class TodoItem(models.Model):
    user = models.ForeignKey(User, default=None)
    todo = models.CharField(max_length=100)
    done_flag = models.BooleanField()
    add_time = models.DateTimeField(auto_now=True)
    priority = models.IntegerField()
    due_time = models.DateTimeField()
    estimated_pomodoroes = models.IntegerField()
    current_pomodores = models.IntegerField(default=0)
    class Meta:
        unique_together = ('user', 'todo')
    def __str__(self):
        return self.todo

class Pomodoro(models.Model):
    todo = models.ForeignKey(TodoItem)
    date = models.DateField(default=None)
    start_time = models.TimeField(default=None)
    completed_flag = models.BooleanField()
    def __str__(self):
        return self.todo.todo+' potato'
class ScheduleItem(models.Model):
    user = models.ForeignKey(User, default=None)
    routine = models.CharField(max_length=100)
    time = models.DateTimeField()
    estimated_duration = models.DurationField()
    loop_time = models.IntegerField(default=0)
    class Meta:
        unique_together = ('user', 'routine')
    def __str__(self):
        return self.routine

class Tag(models.Model):
    tag = models.CharField(max_length=20, primary_key=True)
    def __str__(self):
        return self.tag

class TagAndTodo(models.Model):
    tag = models.ForeignKey(Tag, default=None)
    todo = models.ForeignKey(TodoItem, default=None)
    class Meta:
        unique_together = ('tag', 'todo')

class TagAndSchedule(models.Model):
    tag = models.ForeignKey(Tag, default=None)
    routine = models.ForeignKey(ScheduleItem, default=None)
    class Meta:
        unique_together = ('tag', 'routine')

class HealthLog(models.Model):
    user = models.ForeignKey(User, default=None)
    date = models.DateField()
    steps = models.IntegerField()
    active_time = models.DurationField()
    when_to_sleep = models.DateTimeField()
    when_to_wake = models.DateTimeField()
    sleep_quality = models.IntegerField()
    def __str__(self):
        return self.date
