from django.urls import path

from tests.test_app_namespaces.drf.views import BlankV1View

urlpatterns = [
    path("blank/", BlankV1View.as_view(), name="blank"),
]
