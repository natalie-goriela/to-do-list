from django.test import TestCase
from django.urls import reverse
from task_manager.models import Tag, Task


TASK_URL = reverse("task_manager:index")
TAG_URL = reverse("task_manager:tag-list")


class ModelTests(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="Test")
        self.assertEqual(str(tag), tag.name)

    def test_task_str(self):
        tag = Tag.objects.create(name="Test")
        task = Task.objects.create(
            content="Test content"
        )
        task.tags.add(tag)
        self.assertEqual(str(task), task.content)


class CreateTagTests(TestCase):
    def test_create_tag(self) -> None:
        self.tag = Tag.objects.create(
            name="Test",
        )
        response = self.client.get(TAG_URL)

        all_tags = Tag.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["tag_list"]), list(all_tags))


class CreateTaskTests(TestCase):
    def test_create_task(self):
        tag = Tag.objects.create(name="Test")
        self.task = Task.objects.create(
            content="Test",
        )
        self.task.tags.add(tag)
        response = self.client.get(TASK_URL)

        all_tasks = Task.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["task_list"]), list(all_tasks))
