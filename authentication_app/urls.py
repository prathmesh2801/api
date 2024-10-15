from django.urls import path
from .views import (RegisterView,LoginView,ChangePasswordView,
                    SendOTPViewEmail,VerifyOTPViewEmail,SendPhoneOTPView,VerifyPhoneOTPView,
                    DeleteUserView,InstantDeleteUserView,LogoutView,RegisterDetailView,RegisterListView,PasswordResetRequestView,
                    PasswordResetConfirmView)
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view(), name='login'),
    path('changepassword/', ChangePasswordView.as_view(), name='change_password'),
    path('email-send-otp/', SendOTPViewEmail.as_view(), name='send_otp'),
    path('email-verify-otp/', VerifyOTPViewEmail.as_view(), name='verify_otp'),
    path('send-phone-otp/', SendPhoneOTPView.as_view(), name='send_phone_otp'), 
    path('verify-phone-otp/', VerifyPhoneOTPView.as_view(), name='verify_phone_otp'),
    path('delete-user/', DeleteUserView.as_view(), name='delete_user'),
    path('instant-delete-user/', InstantDeleteUserView.as_view(), name='instant_delete_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', RegisterListView.as_view(), name='register-list'),
    path('profile/<int:pk>/', RegisterDetailView.as_view(), name='register-detail'),
    path('passwordreset/',PasswordResetRequestView.as_view(),name="reset password"),
    path('passwordconfirm/',PasswordResetConfirmView.as_view(),name='reset_password_confirmation')
]
