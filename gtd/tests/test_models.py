from django.test import TestCase
from gtd.models import (
    User, ScheduleItem, TodoItem, Pomodoro, Tag,
    HealthLog, TagAndSchedule, TagAndTodo
)

class UserModelTest(TestCase):
    def test_can_add_a_new_user(self):
        pass
