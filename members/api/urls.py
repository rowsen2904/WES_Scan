from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import MemberViewSet, SpecializationViewSet, DateMemberAPIView, MemberQRCode

urlpatterns = [
    path("date/member/<slug:slug>/", DateMemberAPIView.as_view()),
    path("qrcode/<str:slug>/", MemberQRCode.as_view())
]

router = SimpleRouter()
router.register('members', MemberViewSet)
router.register('specializations', SpecializationViewSet)
urlpatterns += router.urls
