from django.apps import AppConfig


class TestAppConfig(AppConfig):
    name = "tests.test_app_simple"

    class DFMeta:
        api_path = "test_app_simple/"
