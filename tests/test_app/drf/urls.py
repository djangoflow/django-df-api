from django.urls import path

from tests.test_app.drf.views import BlankView

urlpatterns = [
    path("blank/", BlankView.as_view(), name="blank"),
]
