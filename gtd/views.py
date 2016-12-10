from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from gtd.models import ScheduleItem, TodoItem, Pomodoro
# Create your views here.

def home_page(request):
    schedules = ScheduleItem.objects.order_by('time')
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
        try:
            which_todo =  TodoItem.objects.get(id=request.POST['which_todo'])
            start_time_ = request.POST['start_time']
            date_ = request.POST['date_time']
            flag = request.POST['flag']
            # numbers = request.POST['pomodoro_numbers']
            Pomodoro.objects.create(todo=which_todo,
                date=date_,
                start_time=start_time_,
                completed_flag=flag
            )
            # for i in numbers:
            #     Pomodoro.objects.create(todo=which_todo,
            #         start_time=date_time,
            #         )
            return HttpResponse("Succeeds.")
        except Exception:
            return HttpResponseNotFound('Wrong!!!')
    else:
        return HttpResponseNotFound('Are you kidding?')
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
