from typing import Any

from django.http import HttpRequest
from rest_framework import views
from rest_framework.response import Response


class BlankV2View(views.APIView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> Response:
        return Response({"message": "blank-v2"})
