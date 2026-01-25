from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TodoTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="test1234"
        )

    def test_create_task(self):
        self.client.login(username="testuser", password="test1234")

        response = self.client.post('/home/', {
            'title': 'Test Task',
            'description': 'Testing',
            'due_date': '2026-01-30',
            'priority': 'High'
        })

        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, "Test Task")
