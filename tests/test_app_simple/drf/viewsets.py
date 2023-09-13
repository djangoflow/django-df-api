from rest_framework.viewsets import ModelViewSet

from df_api_drf.drf.permissions import IsOwnerOrReadOnly
from df_api_drf.drf.viewsets import ModelOwnerViewSet
from tests.test_app_simple.drf.serializers import (
    NoteSerializer,
    PostSerializer,
)
from tests.test_app_simple.models import Note, Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer: PostSerializer) -> None:
        serializer.save(author=self.request.user)


class NoteViewSet(ModelOwnerViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer: NoteSerializer) -> None:
        serializer.save(author=self.request.user)
