from rest_framework import serializers
from .models import yo

class yoSerializer(serializers.ModelSerializer):
    class Meta:
        model = yo
        fields = '__all__'