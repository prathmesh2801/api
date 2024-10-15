from django.urls import path
from .views import (
    UserModelAPIView, SixPhotoAPIView, IdProofAPIView, DocumentAddressAPIView, 
    CompatibilityMatchAPIView, ReviewSectionAPIView, HabitsDetailsAPIView, 
    HobbiesDetailsAPIView, ProfileCompletesAPIView, HoroscopeDetailsAPIView
)

urlpatterns = [
    # UserModel URLs
    path('users/', UserModelAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserModelAPIView.as_view(), name='user-detail'),

    # SixPhoto URLs
    path('six-photo/', SixPhotoAPIView.as_view(), name='six-photo-list-create'),
    path('six-photo/<int:pk>/', SixPhotoAPIView.as_view(), name='six-photo-detail'),

    # IdProof URLs
    path('id-proof/', IdProofAPIView.as_view(), name='id-proof-list-create'),
    path('id-proof/<int:pk>/', IdProofAPIView.as_view(), name='id-proof-detail'),

    # DocumentAddress URLs
    path('document-address/', DocumentAddressAPIView.as_view(), name='document-address-list-create'),
    path('document-address/<int:pk>/', DocumentAddressAPIView.as_view(), name='document-address-detail'),

    # CompatibilityMatch URLs
    path('compatibility-match/', CompatibilityMatchAPIView.as_view(), name='compatibility-match-list-create'),
    path('compatibility-match/<int:pk>/', CompatibilityMatchAPIView.as_view(), name='compatibility-match-detail'),

    # ReviewSection URLs
    path('review-section/', ReviewSectionAPIView.as_view(), name='review-section-list-create'),
    path('review-section/<int:pk>/', ReviewSectionAPIView.as_view(), name='review-section-detail'),

    # HabitsDetails URLs
    path('habits/', HabitsDetailsAPIView.as_view(), name='habits-list-create'),
    path('habits/<int:pk>/', HabitsDetailsAPIView.as_view(), name='habits-detail'),

    # HobbiesDetails URLs
    path('hobbies/', HobbiesDetailsAPIView.as_view(), name='hobbies-list-create'),
    path('hobbies/<int:pk>/', HobbiesDetailsAPIView.as_view(), name='hobbies-detail'),

    # HoroscopeDetails URLs
    path('horoscope/', HoroscopeDetailsAPIView.as_view(), name='horoscope-list-create'),
    path('horoscope/<int:pk>/', HoroscopeDetailsAPIView.as_view(), name='horoscope-detail'),

    # ProfileCompletes URLs
    path('profile-completes/', ProfileCompletesAPIView.as_view(), name='profile-completes-list-create'),
    path('profile-completes/<int:pk>/', ProfileCompletesAPIView.as_view(), name='profile-completes-detail'),
]
