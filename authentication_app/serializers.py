from rest_framework import serializers
from .models import Register

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = [
            'email', 
            'name', 
            'password', 
            'phone_number', 
            'gender', 
            'dob', 
            'birthplace', 
            'education'
        ]
    

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data
    



