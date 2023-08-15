from django.urls import path

from tests.test_app_namespaces.drf_v2.views import BlankV2View

urlpatterns = [
    path("blank/", BlankV2View.as_view(), name="blank"),
]
