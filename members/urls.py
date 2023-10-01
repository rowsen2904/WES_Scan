from django.urls import path

from .views import MemberListView, redirect_view

urlpatterns = [
    path("", redirect_view, name="redirect-view"),
    path("members/", MemberListView.as_view(), name="members-list"),
]

