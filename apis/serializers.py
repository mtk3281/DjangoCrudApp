from rest_framework import serializers
from webapp.models import record  
from django.contrib.auth import get_user_model
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = record
        fields = '__all__'  


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields =[
        "username",
        "first_name",
        "last_name",
        "email",
        "dob",
        "is_staff",
        "groups",
]