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

    def test_get_single_todo(self):
        response = self.client.get(f"/api/todos/{self.todo.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.todo.title)

    def test_update_todo(self):
        data = {
            "title": "Updated task",
            "description": "Updated description",
            "is_completed": True
        }

        response = self.client.put(f"/api/todos/{self.todo.id}/", data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todo(self):
        response = self.client.delete(f"/api/todos/{self.todo.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_empty_title_validation(self):
        data = {
            "title": "   ",
            "description": "Invalid"
        }

        response = self.client.post("/api/todos/", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_home_endpoint(self):
        response = self.client.get("/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["message"], "Todo API is running")
        self.assertEqual(response.json()["endpoints"], "/api/todos/")