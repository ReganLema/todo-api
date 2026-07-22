from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task


class TaskTest(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="regan",
            password="password123"
        )

        response = self.client.post(
            reverse("login"),
            {
                "username": "regan",
                "password": "password123"
            }
        )

        token = response.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token}"
        )





#Test Create Task

    def test_create_task(self):

        response = self.client.post(

            reverse("task-list"),

            {
                "title": "Study Django",
                "description": "CRUD"
            }

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Task.objects.count(),
            1
        )





#Test List Tasks
    def test_list_tasks(self):

        Task.objects.create(
            owner=self.user,
            title="Task One"
        )

        response = self.client.get(
            reverse("task-list")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.data["results"]),
            1
        )





