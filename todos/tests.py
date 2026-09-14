from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskModelTests(TestCase):
    def test_create_task_defaults(self):
        task = Task.objects.create(title="Learn CI/CD")
        self.assertEqual(task.title, "Learn CI/CD")
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.created_at)

    def test_str_returns_title(self):
        self.assertEqual(str(Task.objects.create(title="Buy milk")), "Buy milk")


class TaskViewTests(TestCase):
    def test_list_page_loads(self):
        response = self.client.get(reverse("todos:task_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Todo List")

    def test_list_shows_tasks(self):
        Task.objects.create(title="Write tests")
        response = self.client.get(reverse("todos:task_list"))
        self.assertContains(response, "Write tests")

    def test_add_task(self):
        response = self.client.post(reverse("todos:task_list"), {"title": "Ship it"})
        self.assertEqual(response.status_code, 302)  # redirect after POST
        self.assertTrue(Task.objects.filter(title="Ship it").exists())

    def test_add_blank_title_creates_nothing(self):
        response = self.client.post(reverse("todos:task_list"), {"title": "   "})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)

    def test_toggle_task(self):
        task = Task.objects.create(title="Toggle me")
        self.client.post(reverse("todos:toggle_task", args=[task.id]))
        task.refresh_from_db()
        self.assertTrue(task.completed)

    def test_toggle_requires_post(self):
        task = Task.objects.create(title="Toggle me")
        response = self.client.get(reverse("todos:toggle_task", args=[task.id]))
        self.assertEqual(response.status_code, 405)
        task.refresh_from_db()
        self.assertFalse(task.completed)

    def test_delete_task(self):
        task = Task.objects.create(title="Delete me")
        response = self.client.post(reverse("todos:delete_task", args=[task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
