from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from gtd.models import ScheduleItem, TodoItem, Pomodoro
import time, datetime
from django.utils import timezone
from django.core.exceptions import ValidationError, ObjectDoesNotExist
# Create your views here.

# 数据规范：
# 早上：8:15-9:55 10:15-11:55 or 8:15-10:10 10:25-11:50 25*4+5*3+15+25*3+5*2  7
# 下午：13:50-16:25 16:45-18:25 or 13:50-15:45 16:00-17:55 25*4+5*3+15+25*4+5*3 8
# 晚上：19:20-9:00 or 19:20-20:45 and 10:00-10:55 25*3+5*3+25*2+5*1 5
# Sleep block/First Class/Second class/Third class/Fourth class/Fifth class/

    # 'Mon': {'Mor': [4, 3], 'Aft': [4, 4], 'Eve': [3, 2]},

# divide time in to 4 blocks


# 生成每周计划
# 先插入schedule
# 检查截止日期在本周内的未完成的todo，如果预计番茄数已经为负数了，将原先的预计*150%直至非负，并提高一级优先级
# 番茄的插入顺序按优先级
# 如果预计番茄数大于剩余时间，
#   输出caution，等比例压缩预计番茄数填充本周计划
# 如果预计番茄数小于剩余时间，
#   找出所有不在本周内的todo，将它们的番茄数除以距离ddl天数平均填充剩余时间

class MyBlock(object):
    def __init__(self, name, schedule, pomodoro):
        self.name = name
        self.schedule = schedule
        self.pomodoro = pomodoro

class Planner(object):
    def get_block_place(self, sourcetime):
        sourcetime_hour = sourcetime.hour
        if 0 <= sourcetime.hour < 6:
            sourcetime_hour += 6
        return (sourcetime.weekday(), int(sourcetime_hour/6)-1)

    def init_my_week(self):
        self.my_week = []
        for i in range(7):
            self.my_week.append([
                # MyBlock('凌晨', [], 0),
                MyBlock('早上', [], 7),
                MyBlock('下午', [], 8),
                MyBlock('晚上', [], 5),
                # {'name': '凌晨', 'schedule': [], 'pomodoro': 0},
                # {'name': '早上', 'schedule': [], 'pomodoro': 7},
                # {'name': '下午', 'schedule': [], 'pomodoro': 8},
                # {'name': '晚上', 'schedule': [], 'pomodoro': 5}
            ])

    def generate_week_plan(self):
        today = timezone.now().date()
        next_day = today+datetime.timedelta(weeks=1)
        this_week_shedules = ScheduleItem.objects.filter(start_time__gt = today, start_time__lt = next_day)
        for schedule in this_week_shedules:
            which_day, which_block = self.get_block_place(schedule.start_time)
            self.my_week[which_day][which_block].schedule.append(schedule.routine)

    def get_today_plan(self):
        # week_day = int(time.strftime("%w"))
        today = timezone.now().date()
        week_day = today.weekday()
        self.init_my_week()
        self.generate_week_plan()

        return self.my_week[week_day]

def home_page(request):
    today = timezone.now().date()
    schedules = ScheduleItem.objects.filter(start_time__gt = today).order_by('start_time')
    todos = TodoItem.objects.filter(done_flag = False).order_by('priority')
    planner = Planner()
    today_plan = planner.get_today_plan()
    return render(request, 'home.html', {
        'my_schedules': schedules[:5],
        'my_todos': todos[:5],
        'my_week': planner.my_week,
        'my_day': today_plan
    })

def view_all(request):
    pass

def login(request):
    pass

# def new_pomodoro(request):
#     pass

def view_pomodoro(request, todo_id):
    todo_item = TodoItem.objects.get(id=todo_id)
    return render(request, 'pomodoro.html', {'todo_item': todo_item})

def post_pomodoro(request):
    if request.method == 'POST':
        # try:
        if True:
            which_todo =  TodoItem.objects.get(id=request.POST['which_todo'])
            hour, minute = request.POST['start_time'].split(':')
            year, month, date = request.POST['date_time'].split('-')
            if request.POST.get('flag') == None:
                flag = True
            else:
                flag = False

            # numbers = request.POST['pomodoro_numbers']
            Pomodoro.objects.create(
                todo=which_todo,
                start_time=datetime.datetime(int(year), int(month), int(date), int(hour), int(minute)),
                completed_flag=flag
            )
            return HttpResponse("Succeeds.")
        # except Exception:
        #     return HttpResponseNotFound('Wrong!!!')
    else:
        return HttpResponseNotFound('Are you kidding?')

def new_pomodoro(request, todo_id):
    try:
        duration_ = request.GET['duration']
    except KeyError:
        duration_ = 25
    try:
        which_todo =  TodoItem.objects.get(id=todo_id)
        Pomodoro.objects.create(
            todo=which_todo,
            start_time=datetime.datetime.now(),
            duration=duration_,
            completed_flag=True
        )
        return HttpResponse('Insertion succeeds.')
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No such todo to record')

def new_schedule(request):
    pass

def view_schedule(request):
    pass

def view_health(request):
    pass

def import_health(request):
    pass

def export_health(request):
    pass

#Todo
# 给过期的土豆和日程修改颜色
# tag系统，按照tag搜索
