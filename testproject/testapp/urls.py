"""test_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from trench import __version__


schema_view = get_schema_view(
   openapi.Info(
        title="django-trench",
        default_version=__version__,
        description="django-trench provides a set of REST API endpoints to supplement django-rest-framework with "
                    "multi-factor authentication (MFA, 2FA)",
        license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('trench.urls')),
    url(r'^auth/', include('trench.urls.jwt')),
    url(r'^simplejwt-auth/', include('trench.urls.simplejwt')),
    url(r'^djoser/', include('djoser.urls')),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
