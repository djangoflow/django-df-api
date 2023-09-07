from django.urls import path

from tests.test_app_simple.drf.views import BlankView, ExtraDataErrorView

urlpatterns = [
    path("blank/", BlankView.as_view(), name="blank"),
    path("extra-data-error/", ExtraDataErrorView.as_view(), name="extra-data-error"),
]
