from django.shortcuts import render, redirect
from django.urls import reverse
import os
import stripe

# Create your views here.
stripe.api_key = os.environ.get('TEST_SECRET_KEY')

def calculate_order_amount(items):
    # Replace this constant with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    return 1400

def payments(request):
    context = {}
    return render(request, 'payments/payments.html', context)

def charge(request):
    amount = []
    if request.method == 'POST':
        print('Data:', request.POST)

    return redirect(reverse('success', args=[amount]))

def successMsg(request, args):
    amount = args
    context = {}
    return render(request, 'payments/success.html', context)