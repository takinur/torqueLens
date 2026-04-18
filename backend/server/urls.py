from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def healthcheck(_request):
    return HttpResponse("Django starter is running.")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", healthcheck),
]
