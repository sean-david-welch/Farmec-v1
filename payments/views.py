from django.shortcuts import render, redirect
from django.urls import reverse
import os
import stripe

# Create your views here.
stripe.api_key = os.environ.get('TEST_SECRET_KEY')

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