from rest_framework import serializers


class DateField(serializers.RelatedField):
    def to_representation(self, value):
        return value.date
