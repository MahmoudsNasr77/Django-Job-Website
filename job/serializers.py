from rest_framework import serializers
from .models import Job
class jobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'