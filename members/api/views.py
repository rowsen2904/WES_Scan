from datetime import datetime

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from helpers.shortcuts import get_object_from_qs_or_404
from members.filters import MemberFilter
from members.models import Member, Specialization
from members.pagination import MemberPagination

from .serializers import MemberSerializer, SpecializationSerializer


class MemberViewSet(ModelViewSet):
    queryset = (
        Member.objects.all()
        .prefetch_related("specializations")
        .prefetch_related("activities")
    )
    serializer_class = MemberSerializer
    pagination_class = MemberPagination
    filterset_class = MemberFilter


class SpecializationViewSet(ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class DateMemberAPIView(APIView):
    def get(self, request, slug):
        model = get_object_from_qs_or_404(Member, slug=slug)
        model.update_last_activity()
        return Response(status=200)


class MemberQRCode(APIView):
    def get_data_success(self, data):
        return {
            "success": True,
            "data": {
                "id": data.id,
                "fullname": data.fullname,
            },
        }

    def get_data_failure(self, message):
        return {
            "success": False,
            "message": f"{message}",
        }

    def get(self, request, slug):
        member = get_object_from_qs_or_404(Member, slug=slug)
        is_updated = member.is_activity_updated()
        if is_updated:
            return Response(self.get_data_success(data=member), status=200)
        return Response(
            self.get_data_failure(message="User already signed in"), status=403
        )
