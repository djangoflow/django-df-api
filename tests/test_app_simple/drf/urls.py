from django.urls import path
from rest_framework.routers import DefaultRouter

from tests.test_app_simple.drf.views import BlankView, ExtraDataErrorView
from tests.test_app_simple.drf.viewsets import NoteViewSet, PostViewSet

urlpatterns = [
    path("blank/", BlankView.as_view(), name="blank"),
    path("extra-data-error/", ExtraDataErrorView.as_view(), name="extra-data-error"),
]

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("notes", NoteViewSet, basename="notes")

urlpatterns += router.urls
