import os
import json
import stripe
import stripe.error
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from . models import PaymentProduct

# Create your views here.
stripe.api_key = os.environ.get('TEST_SECRET_KEY')



class SucessView(TemplateView):
    template_name = 'payments/success.html'

class CancelView(TemplateView):
    template_name = 'payments/cancel.html'


class PaymentsLandingPageView(TemplateView):
    template_name = 'payments/payments.html'

    def get_context_data(self, **kwargs):
        product = PaymentProduct.objects.get(name='Test Product')
        context = super(PaymentsLandingPageView, self).get_context_data(**kwargs)
        context.update({
            'product': product,
            'TEST_PUBLIC_KEY': os.environ.get('TEST_PUBLIC_KEY'),
        })
        return context

class IntentsLandingPageView(TemplateView):
    template_name = 'payments/intent.html'

    def get_context_data(self, **kwargs):
        product = PaymentProduct.objects.get(name='Test Product')
        context = super(IntentsLandingPageView, self).get_context_data(**kwargs)
        context.update({
            'product': product,
            'TEST_PUBLIC_KEY': os.environ.get('TEST_PUBLIC_KEY'),
        })
        return context

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = PaymentProduct.objects.get(id=product_id)
        YOUR_DOMAIN = os.environ.get('YOUR_DOMAIN')
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })
    
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, os.environ.get('STRIPE_WEBHOOK_SECRET')
        )
    except ValueError as e:
        return HttpResponse(status=400) 
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        customer_email = session['customer_detail']['email']
        product_id = session['metadata']['product_id']

        product = PaymentProduct.objects.get(id=product_id)

        send_mail (
            subject = 'Here is your product',
            message = f'Thanks for your purchase, here is the product you ordered, find it here at {product.url}',
            recipient_list= [customer_email],
            from_email= ['jennie@farmec.ie'],
        )
    
    return HttpResponse(status=200)

class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            try:
                product_id = self.kwargs['pk']
                product = PaymentProduct.objects.get(id=product_id)
                intent = stripe.PaymentIntent.create(
                    amount=product.price,
                    currency='usd',
                    metadata={
                        "product_id": product.id
                    }
                )
                return JsonResponse({
                    'clientSecret': intent.client_secret
                })
            except Exception as e:
                return JsonResponse({'error': str(e) }) 
         


