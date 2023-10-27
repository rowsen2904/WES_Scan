from rest_framework import serializers

from helpers.serializers import DateField
from members.models import Member, Specialization


class MemberSerializer(serializers.ModelSerializer):
    activities = DateField(read_only=True, many=True)

    class Meta:
        model = Member
        fields = ["id", "fullname", "email", "birth_date", "phone_number",
                  "gender", "specializations", "activities", "image", ]


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"
