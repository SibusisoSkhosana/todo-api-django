from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Todo


class TodoApiTests(APITestCase):

    def setUp(self):
        self.todo = Todo.objects.create(
            title="Release song",
            description="Write a 16 bar verse and record vocals"
        )

    def test_create_todo(self):
        data = {
            "title": "Submit demo code project",
            "description": "Complete code and submit asap"
        }

        response = self.client.post("/api/todos/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 2)

    def test_list_todos(self):
        response = self.client.get("/api/todos/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
