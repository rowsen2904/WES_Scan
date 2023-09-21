from rest_framework.viewsets import ModelViewSet

from .serializers import MemberSerializer, SpecializationSerializer
from members.filters import MemberFilter
from members.models import Member, Specialization
from members.pagination import MemberPagination


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all().prefetch_related('specializations').prefetch_related('dates')
    serializer_class = MemberSerializer
    pagination_class = MemberPagination
    filterset_class = MemberFilter


class SpecializationViewSet(ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
