from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DFApiConfig(AppConfig):
    name = "df_api"
    verbose_name = _("DjangoFlow API")

    def ready(self):
        ...
        # import urls
        # urlpatterns = [...]
        # urls.append(urlpatterns)
