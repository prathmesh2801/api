from django.shortcuts import render
import razorpay
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#code to genrate random payment id for verification purpose dummy payment id
import random
import string

# Function to generate a random payment_id (starts with 'pay_')
def generate_payment_id():
    return "pay_" + ''.join(random.choices(string.ascii_letters + string.digits, k=14))


#code to genrate random signature for verification purpose dummy signature
import hashlib
import hmac

def generate_signature(order_id, payment_id, secret):
    message = f"{order_id}|{payment_id}"
    return hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest()





class CreateRazorpayOrder(APIView):
    def post(self, request):
        amount = request.data.get('amount')
        
        # Initialize Razorpay client
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        # Create Razorpay order
        order_data = {
            'amount': amount * 100,  # Razorpay accepts amount in paise
            'currency': 'INR',
            'payment_capture': '1'  # automatic capture after successful payment
        }

        order = client.order.create(data=order_data)

        # generate payment id and signature after order id generation dummy
        payment_id = generate_payment_id()
        signature = generate_signature(order['id'], payment_id, settings.RAZORPAY_KEY_SECRET)

        # Return order id to the frontend
        return Response({
            'order_id': order['id'],
            'amount': amount,
            'currency': 'INR',
            'payment_id': payment_id,
            'signature': signature,
            'status': 'Created'
        })



class VerifyRazorpayPayment(APIView):
    def post(self, request):
        order_id = request.data.get('order_id')
        payment_id = request.data.get('payment_id')
        signature = request.data.get('signature')

        # Initialize Razorpay client
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        # Verify payment signature
        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        try:
            client.utility.verify_payment_signature(params_dict)
            return Response({'status': 'Payment verified'})
    
        except:
            return Response({'error': 'Invalid signature'})



