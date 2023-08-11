from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class DfApiTests(APITestCase):
    """Tests for DF API."""

    def test_blank_view_returns_204(self) -> None:
        url = reverse("df_api:blank")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
