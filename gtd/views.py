from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from gtd.models import ScheduleItem, TodoItem, Pomodoro
import time, datetime
from django.utils import timezone
from django.core.exceptions import ValidationError, ObjectDoesNotExist
# Create your views here.

# week_plan = {
#     'today': []
# }
#
#
# def generate_week_plan():
#     today = timezone.now().today()
#     next_day = today+datetime.timedelta(weeks=1)
#     this_week_shedules = ScheduleItem.objects.filter(time__gt = today, time__lt = next_day)
#
# def get_plan():
#     pass　

def home_page(request):
    schedules = ScheduleItem.objects.order_by('start_time')
    todos = TodoItem.objects.order_by('priority')
    return render(request, 'home.html', {
        'my_schedules': schedules,
        'my_todos': todos,
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
