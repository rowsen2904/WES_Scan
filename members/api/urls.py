from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import MemberViewSet, SpecializationViewSet

urlpatterns = [

]

router = SimpleRouter()
router.register('members', MemberViewSet)
router.register('specializations', SpecializationViewSet)
urlpatterns += router.urls
