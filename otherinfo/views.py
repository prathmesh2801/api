from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import UserModel, SixPhoto, IdProof, DocumentAddress, CompatibilityMatch, ReviewSection, HabitsDetails, HobbiesDetails, ProfileCompletes, HoroscopeDetails
from .serializers import (
    UserModelSerializer, SixPhotoSerializer, IdProofSerializer, DocumentAddressSerializer, 
    CompatibilityMatchSerializer, ReviewSectionSerializer, HabitsDetailsSerializer, 
    HobbiesDetailsSerializer, ProfileCompletesSerializer, HoroscopeDetailsSerializer
)

# UserModel API Views
class UserModelAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            user_model = get_object_or_404(UserModel, pk=pk)
            serializer = UserModelSerializer(user_model)
            return Response(serializer.data)
        else:
            user_model = UserModel.objects.all()
            serializer = UserModelSerializer(user_model, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user_model = get_object_or_404(UserModel, pk=pk)
        serializer = UserModelSerializer(user_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        user_model = get_object_or_404(UserModel, pk=pk)
        serializer = UserModelSerializer(user_model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_model = get_object_or_404(UserModel, pk=pk)
        user_model.delete()
        return Response({"message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)


# SixPhoto API Views
class SixPhotoAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            six_photo = get_object_or_404(SixPhoto, pk=pk)
            serializer = SixPhotoSerializer(six_photo)
            return Response(serializer.data)
        else:
            six_photo = SixPhoto.objects.all()
            serializer = SixPhotoSerializer(six_photo, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = SixPhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        six_photo = get_object_or_404(SixPhoto, pk=pk)
        serializer = SixPhotoSerializer(six_photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        six_photo = get_object_or_404(SixPhoto, pk=pk)
        serializer = SixPhotoSerializer(six_photo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        six_photo = get_object_or_404(SixPhoto, pk=pk)
        six_photo.delete()
        return Response({"message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)


# IdProof API Views
class IdProofAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            id_proof = get_object_or_404(IdProof, pk=pk)
            serializer = IdProofSerializer(id_proof)
            return Response(serializer.data)
        else:
            id_proof = IdProof.objects.all()
            serializer = IdProofSerializer(id_proof, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = IdProofSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        id_proof = get_object_or_404(IdProof, pk=pk)
        serializer = IdProofSerializer(id_proof, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        id_proof = get_object_or_404(IdProof, pk=pk)
        serializer = IdProofSerializer(id_proof, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        id_proof = get_object_or_404(IdProof, pk=pk)
        id_proof.delete()
        return Response({"message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)


# DocumentAddress API Views
class DocumentAddressAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            documents_add = get_object_or_404(DocumentAddress, pk=pk)
            serializer = DocumentAddressSerializer(documents_add)
            return Response(serializer.data)
        else:
            documents_add = DocumentAddress.objects.all()
            serializer = DocumentAddressSerializer(documents_add, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = DocumentAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        documents_add = get_object_or_404(DocumentAddress, pk=pk)
        serializer = DocumentAddressSerializer(documents_add, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        documents_add = get_object_or_404(DocumentAddress, pk=pk)
        serializer = DocumentAddressSerializer(documents_add, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        documents_add = get_object_or_404(DocumentAddress, pk=pk)
        documents_add.delete()
        return Response({"message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)


# Compatibility Match API Views
class CompatibilityMatchAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            compatibility_match = get_object_or_404(CompatibilityMatch, pk=pk)
            serializer = CompatibilityMatchSerializer(compatibility_match)
            return Response(serializer.data)
        else:
            compatibility_match = CompatibilityMatch.objects.all()
            serializer = CompatibilityMatchSerializer(compatibility_match, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CompatibilityMatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        compatibility_match = get_object_or_404(CompatibilityMatch, pk=pk)
        serializer = CompatibilityMatchSerializer(compatibility_match, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        compatibility_match = get_object_or_404(CompatibilityMatch, pk=pk)
        serializer = CompatibilityMatchSerializer(compatibility_match, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        compatibility_match = get_object_or_404(CompatibilityMatch, pk=pk)
        compatibility_match.delete()
        return Response({"message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)


# Review Section API Views
class ReviewSectionAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            review_section = get_object_or_404(ReviewSection, pk=pk)
            serializer = ReviewSectionSerializer(review_section)
            return Response(serializer.data)
        else:
            review_section = ReviewSection.objects.all()
            serializer = ReviewSectionSerializer(review_section, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        review_section = get_object_or_404(ReviewSection, pk=pk)
        serializer = ReviewSectionSerializer(review_section, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        review_section = get_object_or_404(ReviewSection, pk=pk)
        serializer = ReviewSectionSerializer(review_section, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review_section = get_object_or_404(ReviewSection, pk=pk)
        review_section.delete()
        return Response({"message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)

# HabitsDetails API Views
class HabitsDetailsAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            habits_details = get_object_or_404(HabitsDetails, pk=pk)
            serializer = HabitsDetailsSerializer(habits_details)
            return Response(serializer.data)
        else:
            habits_details = HabitsDetails.objects.all()
            serializer = HabitsDetailsSerializer(habits_details, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = HabitsDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        habits_details = get_object_or_404(HabitsDetails, pk=pk)
        serializer = HabitsDetailsSerializer(habits_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        habits_details = get_object_or_404(HabitsDetails, pk=pk)
        serializer = HabitsDetailsSerializer(habits_details, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        habits_details = get_object_or_404(HabitsDetails, pk=pk)
        habits_details.delete()
        return Response({"message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)


# HobbiesDetails API Views
class HobbiesDetailsAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            hobbies_details = get_object_or_404(HobbiesDetails, pk=pk)
            serializer = HobbiesDetailsSerializer(hobbies_details)
            return Response(serializer.data)
        else:
            hobbies_details = HobbiesDetails.objects.all()
            serializer = HobbiesDetailsSerializer(hobbies_details, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = HobbiesDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        hobbies_details = get_object_or_404(HobbiesDetails, pk=pk)
        serializer = HobbiesDetailsSerializer(hobbies_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        hobbies_details = get_object_or_404(HobbiesDetails, pk=pk)
        serializer = HobbiesDetailsSerializer(hobbies_details, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        hobbies_details = get_object_or_404(HobbiesDetails, pk=pk)
        hobbies_details.delete()
        return Response({"message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)


# HoroscopeDetails API Views
class HoroscopeDetailsAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            horoscope_details = get_object_or_404(HoroscopeDetails, pk=pk)
            serializer = HoroscopeDetailsSerializer(horoscope_details)
            return Response(serializer.data)
        else:
            horoscope_details = HoroscopeDetails.objects.all()
            serializer = HoroscopeDetailsSerializer(horoscope_details, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = HoroscopeDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        horoscope_details = get_object_or_404(HoroscopeDetails, pk=pk)
        serializer = HoroscopeDetailsSerializer(horoscope_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        horoscope_details = get_object_or_404(HoroscopeDetails, pk=pk)
        serializer = HoroscopeDetailsSerializer(horoscope_details, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        horoscope_details = get_object_or_404(HoroscopeDetails, pk=pk)
        horoscope_details.delete()
        return Response({"message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)


# ProfileCompletes API Views
class ProfileCompletesAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            profile_completes = get_object_or_404(ProfileCompletes, pk=pk)
            serializer = ProfileCompletesSerializer(profile_completes)
            return Response(serializer.data)
        else:
            profile_completes = ProfileCompletes.objects.all()
            serializer = ProfileCompletesSerializer(profile_completes, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ProfileCompletesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        profile_completes = get_object_or_404(ProfileCompletes, pk=pk)
        serializer = ProfileCompletesSerializer(profile_completes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        profile_completes = get_object_or_404(ProfileCompletes, pk=pk)
        serializer = ProfileCompletesSerializer(profile_completes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile_completes = get_object_or_404(ProfileCompletes, pk=pk)
        profile_completes.delete()
        return Response({"message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)


