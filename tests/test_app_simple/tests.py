from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from df_api_drf.resolvers import site_url
from tests.test_app_simple.models import Note, Post

User = get_user_model()


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

    def test_extra_data_error_response_contains_extra_data(self) -> None:
        url = reverse("df_api_drf:v1:test_app_simple:extra-data-error")
        response = self.client.get(url)
        self.assertEqual(response.data["errors"][0]["extra_data"], {"extra": "data"})


class PostApiTests(APITestCase):
    def setUp(self) -> None:
        self.author = User.objects.create_user(username="author")
        self.user = User.objects.create_user(username="user")
        self.author_client = APIClient()
        self.author_client.force_authenticate(user=self.author)
        self.user_client = APIClient()
        self.user_client.force_authenticate(user=self.user)

        self.post = Post.objects.create(
            title="title",
            body="body",
            author=self.author,
        )

    def test_author_can_update_post(self) -> None:
        response = self.author_client.patch(
            f"/api/v1/test_app_simple/posts/{self.post.id}/", {"title": "new title"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "new title")

    def test_user_can_read_post(self) -> None:
        response = self.user_client.get(
            f"/api/v1/test_app_simple/posts/{self.post.id}/",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "title")

    def test_user_cannot_update_post(self) -> None:
        response = self.user_client.patch(
            f"/api/v1/test_app_simple/posts/{self.post.id}/", {"title": "new title"}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class NoteApiTests(APITestCase):
    def setUp(self) -> None:
        self.author = User.objects.create_user(username="author")
        self.user = User.objects.create_user(username="user")
        self.author_client = APIClient()
        self.author_client.force_authenticate(user=self.author)
        self.user_client = APIClient()
        self.user_client.force_authenticate(user=self.user)

        self.note = Note.objects.create(
            title="title",
            body="body",
            author=self.author,
        )

    def test_author_can_update_note(self) -> None:
        response = self.author_client.patch(
            f"/api/v1/test_app_simple/notes/{self.note.id}/", {"title": "new title"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "new title")

    def test_user_cannot_read_note(self) -> None:
        response = self.user_client.get(
            f"/api/v1/test_app_simple/notes/{self.note.id}/",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class BaseURLTests(APITestCase):
    def test_base_url(self) -> None:
        domain_name = "test.com"
        Site.objects.update_or_create(
            id=1,
            defaults={
                "domain": domain_name,
                "name": domain_name,
            },
        )

        assert site_url() == "https://test.com/#"
