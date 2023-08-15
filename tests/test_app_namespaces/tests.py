from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class DfApiTests(APITestCase):
    """Tests for DF API."""

    def test_blank_v1_view_returns_200(self) -> None:
        url = reverse("df_api_drf:v1:test_app_namespaces:blank")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "blank-v1")

    def test_blank_v2_view_returns_200(self) -> None:
        url = reverse("df_api_drf:v2:test_app_namespaces:blank")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "blank-v2")
