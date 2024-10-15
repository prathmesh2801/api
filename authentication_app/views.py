from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from .models import Register
import random
from django.utils import timezone
from django.contrib.auth import logout
from rest_framework_simplejwt.tokens import RefreshToken
#from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # Save the user's data
            user = serializer.save()

            # Prepare and send the email
            subject = 'Registration Successful'
            message = f'Hello {user.name},\n\nYou have successfully registered with the email {user.email}.'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            
            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                return Response({"message": "Registration successful, confirmation email sent!"})
            except Exception as e:
                return Response({"message": "Registration successful, but failed to send confirmation email."})
        
        return Response(serializer.errors)
    



class LoginView(APIView):

    #permission_classes = [IsAuthenticated]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Authenticate user
        try:
            user = Register.objects.get(email=email)
            if user.password == password:
                refresh = RefreshToken.for_user(user)

                return Response({ "Login succesfully"
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return Response({"error": "Invalid credentials"})

        except Register.DoesNotExist:
            return Response({"error": "User does not exist"})




class ChangePasswordView(APIView):
    def post(self, request):
        # Get data from request
        email = request.data.get('email')
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        # Check if email is provided
        if not email:
            return Response({"error": "Email is required"})

        try:
            # Find user by email
            user = Register.objects.get(email=email)

            # Check if the old password matches the user's current password
            if user.password != old_password:
                return Response({"error": "Old password is incorrect"})

            # Ensure the new password and confirm password match
            if new_password != confirm_password:
                return Response({"error": "New password and confirm password do not match"})

            # Update the user's password
            user.password = new_password
            user.save()

            return Response({"message": "Password changed successfully"})

        except Register.DoesNotExist:
            return Response({"error": "User not found"})
        


class SendOTPViewEmail(APIView):
    def post(self, request):
        email = request.data.get('email')

        try:
            user = Register.objects.get(email=email)

            # Generate a random 6-digit OTP
            otp = str(random.randint(100000, 999999))
            user.otp = otp
            user.save()

            subject = 'Your OTP for Email Verification'
            message = f"Hi {user.name},\nYour OTP for email verification is: {otp}\nPlease enter this OTP to verify your email."
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return Response({"message": "OTP sent successfully!"})

        except Register.DoesNotExist:
            return Response({"error": "User with this email does not exist"})
        
class VerifyOTPViewEmail(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')

        try:
            user = Register.objects.get(email=email)
            if user.otp == otp:
                user.save()
                return Response({"message": "Email verified successfully!"})
            else:
                return Response({"error": "Invalid OTP"})

        except Register.DoesNotExist:
            return Response({"error": "User with this email does not exist"})
        


from twilio.rest import Client 

class SendPhoneOTPView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')

        try:
            user = Register.objects.get(phone_number=phone_number)

            # Generate a random 6-digit OTP
            otp = str(random.randint(100000, 999999))
            user.otp = otp
            user.save()

            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

            # Send OTP via Twilio SMS
            message = client.messages.create(
                body=f"Your OTP for phone verification is: {otp}. Please enter this OTP to verify your phone number.",
                from_=settings.TWILIO_PHONE_NUMBER,
                to=phone_number
            )

            return Response({"message": "OTP sent successfully!"})

        except Register.DoesNotExist:
            return Response({"error": "User with this phone number does not exist"})

class VerifyPhoneOTPView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        otp = request.data.get('otp')

        try:
            user = Register.objects.get(phone_number=phone_number)
            if user.otp == otp:
                user.save()
                return Response({"message": "Phone number verified successfully!"})
            else:
                return Response({"error": "Invalid OTP"})

        except Register.DoesNotExist:
            return Response({"error": "User with this phone number does not exist"})
        


class DeleteUserView(APIView):
    def delete(self, request):
        email = request.data.get('email')

        try:
            user = Register.objects.get(email=email)

            # Mark the user for deletion
            user.is_deleted = True
            user.deletion_date = timezone.now() + timezone.timedelta(days=90)  # Set deletion date
            user.save()

            return Response({"message": "User marked for deletion. It will be permanently deleted after 90 days."})

        except Register.DoesNotExist:
            return Response({"error": "User does not exist"})


class InstantDeleteUserView(APIView):
    def delete(self, request):
        email = request.data.get('email')

        try:
            user = Register.objects.get(email=email)
            user.delete()

            return Response({"message": "User deleted successfully."})

        except Register.DoesNotExist:
            return Response({"error": "User does not exist"})
        

class LogoutView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = Register.objects.get(email=email)
        logout(request)
        return Response({"message": "Logged out successfully."})
    



class RegisterListView(APIView):
    def get(self, request):
        users = Register.objects.all()  # Retrieve all users
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data)


class RegisterDetailView(APIView):
    def get(self, request, pk):
        try:
            user = Register.objects.get(pk=pk)  # Retrieve user by ID
        except Register.DoesNotExist:
            return Response({"error": "User not found"})
        
        serializer = RegisterSerializer(user)
        return Response(serializer.data)




class PasswordResetRequestView(APIView):
    def post(self, request):
        email = request.data.get('email')

        # Send password reset link to the user's email
        reset_link = f'http://yourdomain.com/reset-password/'  # Adjust URL as needed
        try:
            send_mail(
                subject='Password Reset Request',
                message=f'Click the link to reset your password: {reset_link}', 
                from_email='prathmesh280199@gmail.com',  # Ensure this is your email
                    recipient_list=[email],
                    fail_silently=False,
                )
        except Exception as e:
            return Response({"error": f"Failed to send email: {str(e)}"})
        return Response({"message": "Password reset link sent to your email."})
    

class PasswordResetConfirmView(APIView):
    def post(self, request):
        email = request.data.get('email')
        new_password=request.data.get('new_password')
        c_new_pass=request.data.get('c_new_pass')


        try:
            user = Register.objects.get(email=email)
            if new_password == c_new_pass:
                user.password = new_password
                user.save()
                return Response({"message": "Password Reset Succesfully...!!"})
            else:
                return Response({"error": "new password and confirm password does not match"})
            
        except Register.DoesNotExist:
            return Response({"error": "User does not exist"})


    

