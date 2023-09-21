from rest_framework import serializers

from ..models import Member, Specialization


class MemberSerializer(serializers.ModelSerializer):
    specializations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # dates = serializers.PrimaryKeyRelatedField(many=True, read_only=True )

    class Meta:
        model = Member
        # fields = "__all__"
        fields = ["fullname", "specializations", "dates", 'image']


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"
