from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import MemberViewSet

# router = SimpleRouter()
# router.register('members', MemberViewSet)
# urlpatterns = router.urls

urlpatterns = [
    path("members/", MemberViewSet.as_view())
]

