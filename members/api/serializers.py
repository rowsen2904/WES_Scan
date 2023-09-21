from rest_framework import serializers

from ..models import Member, Specialization


class SpecializationField(serializers.RelatedField):

    def to_representation(self, value):
        return value.name


class DateField(serializers.RelatedField):

    def to_representation(self, value):
        return value.date


class MemberSerializer(serializers.ModelSerializer):
    specializations = SpecializationField(read_only=True, many=True)
    dates = DateField(read_only=True, many=True)

    class Meta:
        model = Member
        fields = ["fullname", "email", "birth_date", "phone_number",
                  "gender", "specializations", "dates", "image"]


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"
