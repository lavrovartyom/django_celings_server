from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Client


class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse("app:home"))
        self.assertEqual(response.status_code, 200)

    def test_add_client(self):
        post_data = {
            "full_name": "Test User",
            "phone_number": "+7(903)-123-45-67",
            "address": "Советская 57",
            "comment": "Домофон не работает",
        }

        response = self.client.post(reverse("app:home"), post_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"success": True})
        self.assertTrue(Client.objects.filter(full_name="Test User").exists())

        # Проверяем, что дата создания приложения была установлена
        client = Client.objects.get(full_name="Test User")

        self.assertAlmostEqual(
            client.application_date,
            timezone.now(),
            delta=timezone.timedelta(seconds=10),
        )

    def test_add_client_with_invalid_phone_number(self):
        post_data = {
            "full_name": "Test User",
            "phone_number": "9031234567",  # Неправильный формат номера
            "address": "123 Elm Street",
        }
        response = self.client.post(reverse("app:home"), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"success": False})

        # Проверяем, что объект не был создан из-за ошибки валидации
        self.assertFalse(Client.objects.filter(full_name="Test User").exists())
