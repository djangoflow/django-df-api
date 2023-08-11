from typing import Any

from django.http import HttpRequest
from rest_framework import views
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT


class BlankView(views.APIView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> Response:
        return Response(status=HTTP_204_NO_CONTENT)
