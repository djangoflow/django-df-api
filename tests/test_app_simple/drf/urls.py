from django.urls import path

from tests.test_app_simple.drf.views import BlankView

urlpatterns = [
    path("blank/", BlankView.as_view(), name="blank"),
]
