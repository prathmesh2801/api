from rest_framework import serializers
from .models import *

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class SixPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SixPhoto
        fields = '__all__'

class IdProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdProof
        fields = '__all__'

class DocumentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentAddress
        fields = '__all__'

class CompatibilityMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompatibilityMatch
        fields = '__all__'

class ReviewSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewSection
        fields = '__all__'

class HabitsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitsDetails
        fields = '__all__'

class HobbiesDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HobbiesDetails
        fields = '__all__'

class ProfileCompletesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCompletes
        fields = '__all__'


class HoroscopeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoroscopeDetails
        fields = '__all__'
