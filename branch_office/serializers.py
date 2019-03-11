from rest_framework import serializers
from .models import Branch_Office

class Branch_OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch_Office
        fields = '__all__'
