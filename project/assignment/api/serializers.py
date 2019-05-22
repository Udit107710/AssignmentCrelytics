from rest_framework import serializers
from .models import Data, FileData

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        exclude = ('id',)

class FileDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileData
        fields = ['file', 'patient_document']
