from django.test import TestCase
from gtd.models import (
    User, ScheduleItem, TodoItem, Pomodoro, Tag,
    HealthLog, TagAndSchedule, TagAndTodo
)

class UserModelTest(TestCase):
    def test_can_add_a_new_user(self):
        pass


class ScheduleModelTest(TestCase):
    def test_can_save_a_normal_schedule(self):
        pass

    def loop_times_and_loop_types_accord(self):
        # nerver and 'Nope'
        #
        pass

    def loop_and_time_accord(self):
        # never: start_time=end_time
        # forever: end=datetime.datetime.max
        # exact: calculation no wrong
        pass

    def duration_not_exceeds(self):
        pass
