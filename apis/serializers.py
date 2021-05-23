from django.db.models import fields
from rest_framework import serializers
from kjsieit import models


class KjsieitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "content",
            "type",
            "subject",
        )
        model = models.Todo
