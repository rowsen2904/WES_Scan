from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import MemberViewSet

urlpatterns = [

]

router = SimpleRouter()
router.register('members', MemberViewSet)
urlpatterns += router.urls
