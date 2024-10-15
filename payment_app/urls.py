from django.urls import path
from .views import CreateRazorpayOrder, VerifyRazorpayPayment

urlpatterns = [
    path('create-razorpay-order/', CreateRazorpayOrder.as_view(), name='create_razorpay_order'),
    path('verify-razorpay-payment/', VerifyRazorpayPayment.as_view(), name='verify_razorpay_payment'),
]
