from rest_framework import generics

from ..models import Member
from .serializers import MemberSerializer, SpecializationSerializer


class MemberViewSet(generics.ListAPIView):
    queryset = Member.objects.prefetch_related('specializations')
    serializer_class = MemberSerializer
