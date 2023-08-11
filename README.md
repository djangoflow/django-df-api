# Django DF API

Module for automatic including Djangoflow apps API to your project.

## Installation:

1. Install the package

```
pip install django-df-api
```

2. Add the package to your INSTALLED_APPS

```
INSTALLED_APPS = [
    ...
    'df_api',
    ...
]
```

3. Add the package to your urls.py

```

urlpatterns = [
    ...
    path("api/v1/", include("df_api.urls")),
    ...
]
```
