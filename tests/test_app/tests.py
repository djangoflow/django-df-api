from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class DfApiTests(APITestCase):
    """Tests for DF API."""

    def test_blank_view_returns_204(self) -> None:
        url = reverse("df_api_drf:blank")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_schema_returns_valid_openapi_spec(self) -> None:
        url = reverse("df_api_drf:schema")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response["Content-Type"], "application/vnd.oai.openapi; charset=utf-8"
        )
        self.assertGreater(len(response.data), 0)

    def test_redoc_returns_valid_redoc_ui(self) -> None:
        url = reverse("df_api_drf:redoc")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
        self.assertIn("redoc_standalone", response.data)

    def test_swagger_returns_valid_swagger_ui(self) -> None:
        url = reverse("df_api_drf:swagger-ui")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
        self.assertIn("swagger_ui_bundle", response.data)
