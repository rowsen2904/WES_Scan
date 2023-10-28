from django.urls import include, path

urlpatterns = [
    path("", include("members.api.urls")),
]
