import django_filters as filters

from .models import Member


class MemberFilter(filters.FilterSet):
    specialization = filters.CharFilter(field_name="specializations__name", lookup_expr='icontains')
    gender = filters.CharFilter(field_name="gender", lookup_expr='icontains')

    class Meta:
        model = Member
        fields = ['specialization', 'gender']
