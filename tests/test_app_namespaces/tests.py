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

    def test_redoc_v2_returns_valid_redoc_ui(self) -> None:
        url = reverse("df_api_drf:v2:redoc")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
        self.assertIn("redoc_standalone", response.data)

    def test_swagger_v2_returns_valid_swagger_ui(self) -> None:
        url = reverse("df_api_drf:v2:swagger-ui")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
        self.assertIn("swagger_ui_bundle", response.data)

    def test_swagger_v2_returns_valid_schema(self) -> None:
        url = reverse("df_api_drf:v2:schema")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("/api/v2/test_app_namespaces/blank/", response.data["paths"])
        blank_path = response.data["paths"]["/api/v2/test_app_namespaces/blank/"]
        self.assertEqual(
            blank_path["get"]["operationId"], "test_app_namespaces_blank_retrieve"
        )
