from typing import Any

from django.http import HttpRequest
from rest_framework import views
from rest_framework.response import Response

from df_api_drf.exceptions import ExtraDataAPIException


class BlankView(views.APIView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> Response:
        return Response({"message": "blank-simple"})


class ExtraDataErrorView(views.APIView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> Response:
        raise ExtraDataAPIException(extra_data={"extra": "data"})
