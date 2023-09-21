from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from ..models import Member
from .serializers import MemberSerializer, SpecializationSerializer


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all().prefetch_related('specializations').prefetch_related('dates')
    serializer_class = MemberSerializer
