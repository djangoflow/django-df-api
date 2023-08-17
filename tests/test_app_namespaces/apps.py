from django.apps import AppConfig


class TestAppConfig(AppConfig):
    name = "tests.test_app_namespaces"

    class DFMeta:
        api_path = "test_app_namespaces/"
        api_drf_namespaces = {
            "v1": "tests.test_app_namespaces.drf.urls",
            "v2": "tests.test_app_namespaces.drf_v2.urls",
        }
