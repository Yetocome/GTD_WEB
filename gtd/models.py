from django.db import models
import datetime, calendar
from django.utils import timezone
from django.contrib.auth.models import User
import pytz

utc=pytz.UTC


LOOP_TYPES = (
    ('N', '不循环'),
    ('D', '每天'),
    ('W', '每周'),
    ('M', '每月'),
    ('Y', '每年')
)

def add_months(sourcetime, months):
    month = sourcetime.month - 1 + months
    year = int(sourcetime.year + month / 12 )
    month = month % 12 + 1
    day = min(sourcetime.day,calendar.monthrange(year,month)[1])
    return datetime.datetime(year, month, day,
        sourcetime.hour, sourcetime.minute, sourcetime.second)

def add_years(sourcetime, years):
    return datetime.datetime(
        sourcetime.year+years,
        sourcetime.month,
        sourcetime.day,
        sourcetime.hour,
        sourcetime.minute,
        sourcetime.second
    )

# Create your models here.

class TodoItem(models.Model):
    user = models.ForeignKey(User, default=None)
    todo = models.CharField(max_length=100)
    done_flag = models.BooleanField()
    add_time = models.DateTimeField(auto_now=True)
    priority = models.IntegerField()
    due_time = models.DateTimeField()
    estimated_pomodoroes = models.IntegerField()
    description = models.CharField(max_length=250, default="")
    # current_pomodores = models.IntegerField(default=0)
    class Meta:
        unique_together = ('user', 'todo')

    # Derived attribute, get current pomodoro numbers
    @property
    def current_pomodores(self):
        return Pomodoro.objects.filter(todo=self).count()

class Pomodoro(models.Model):
    todo = models.ForeignKey(TodoItem)
    # date = models.DateField(default=None)
    start_time = models.DateTimeField(default=None)
    duration = models.IntegerField(default=25)
    completed_flag = models.BooleanField(default=True)
    def __str__(self):
        return self.todo.todo+' potato'


class ScheduleItem(models.Model):
    user = models.ForeignKey(User, default=None)
    routine = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    estimated_duration = models.DurationField()
    loop_types = models.CharField(max_length=1, default='N', choices=LOOP_TYPES)
    # 0:never 1:daily 7:weekly -1:monthly -2:yearly any-pos:auto_def
    loop_times = models.IntegerField(default=0)
    description = models.CharField(max_length=250, default="")
    # 0:Never Neg: forever


    @property
    def end_time(self):
        tz_info = self.start_time.tzinfo
        ra = None
        if self.loop_times == 0:
            ra = self.start_time
        elif self.loop_times < 0:
            ra =  datetime.datetime.max
        else:
            if self.loop_types == LOOP_TYPES[1][0]:
                ra = self.start_time+datetime.timedelta(days=1)*self.loop_times
            elif self.loop_types == LOOP_TYPES[2][0]:
                ra = self.start_time+datetime.timedelta(weeks=1)*self.loop_times
            elif self.loop_types == LOOP_TYPES[3][0]:
                ra =  add_months(self.start_time, self.loop_times)
            elif self.loop_types == LOOP_TYPES[4][0]:
                ra =  add_years(self.start_time, self.loop_times)
            else:
                raise Exception()
        return ra.replace(tzinfo = tz_info)

    @property
    def next_time(self):
        tz_info = self.start_time.tzinfo
        # now = timezone.now()
        now = datetime.datetime.now(tz_info)

        if self.end_time < now:
            return None

        if self.loop_times == 0:
            return self.start_time
        else: # Could be optimized by dichotomy
            n_time = self.start_time
            n_time = n_time.replace(tzinfo = tz_info)
            if self.loop_types == LOOP_TYPES[1][0]:
                return n_time.replace(now.year, now.month, now.day)
            elif self.loop_types == LOOP_TYPES[2][0]:
                for i in range(self.loop_times):
                    if n_time >= now:
                        return n_time
                    n_time += datetime.timedelta(weeks=1)
                raise Exception()
            elif self.loop_types == LOOP_TYPES[3][0]:
                for i in range(self.loop_times):
                    if n_time >= now:
                        return n_time
                    n_time = add_months(n_time, 1).replace(tzinfo = tz_info)
                raise Exception()
            elif self.loop_types == LOOP_TYPES[4][0]:
                for i in range(self.loop_times):
                    if n_time >= now:
                        return n_time
                    n_time = add_years(n_time, 1).replace(tzinfo = tz_info)
                raise Exception()
            else:
                raise Exception()

    class Meta:
        unique_together = ('user', 'routine')
    # Valitation for set of duration
    def save(self, *args, **kwargs):
        if self.estimated_duration > datetime.timedelta(hours=18):
            raise ValueError("You cannot add a estimated duration more than 18 hours")
        super().save(*args, **kwargs)

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
