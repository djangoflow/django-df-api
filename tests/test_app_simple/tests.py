from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class DfApiTests(APITestCase):
    """Tests for DF API."""

    def test_blank_view_returns_200(self) -> None:
        url = reverse("df_api_drf:v1:test_app_simple:blank")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "blank-simple")

    def test_schema_returns_valid_openapi_spec(self) -> None:
        url = reverse("df_api_drf:v1:schema")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response["Content-Type"], "application/vnd.oai.openapi; charset=utf-8"
        )
        self.assertGreater(len(response.data), 0)

    def test_redoc_returns_valid_redoc_ui(self) -> None:
        url = reverse("df_api_drf:v1:redoc")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
        self.assertIn("redoc_standalone", response.data)

    def test_swagger_returns_valid_swagger_ui(self) -> None:
        url = reverse("df_api_drf:v1:swagger-ui")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
        self.assertIn("swagger_ui_bundle", response.data)

    def test_swagger_returns_valid_schema(self) -> None:
        url = reverse("df_api_drf:v1:schema")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("/api/v1/test_app_namespaces/blank/", response.data["paths"])
        blank_path = response.data["paths"]["/api/v1/test_app_namespaces/blank/"]
        self.assertEqual(
            blank_path["get"]["operationId"], "test_app_namespaces_blank_retrieve"
        )
