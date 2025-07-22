from rest_framework import serializers

from .models import Image_Result, Logs

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_Result
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = '__all__'