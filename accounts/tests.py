from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class RegisterTest(APITestCase):

    def test_register_user(self):

        url = reverse("register")

        data = {
            "username": "regan",
            "email": "regan@gmail.com",
            "password": "password123"
        }

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            User.objects.count(),
            1
        )


        


class LoginTest(APITestCase):

    def setUp(self):

        User.objects.create_user(
            username="regan",
            password="password123"
        )

    def test_login(self):

        url = reverse("login")

        response = self.client.post(
            url,
            {
                "username": "regan",
                "password": "password123"
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIn(
            "access",
            response.data
        )

        self.assertIn(
            "refresh",
            response.data
        )