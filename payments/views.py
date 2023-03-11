# Create your views here.
import os
import stripe
import stripe.error
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from . models import PaymentProduct
from . forms import PaymentProductForm

# Create your views here.
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

##############################
####### Stripe Endpoints #####
##############################
@login_required(login_url='login')
def successview(request): 

    if request.method == 'POST':
        return redirect('home')
    
    context = {}
    return render(request, 'payments/success.html', context)

@login_required(login_url='login')
def cancelview(request): 

    if request.method == 'POST':
        return redirect('payments')
    
    context = {}
    return render(request, 'payments/cancel.html', context)

@login_required(login_url='login')
def stripe_products(request): 
    products = PaymentProduct.objects.all()

    context = {'products': products, }
    return render(request, 'payments/products.html', context)

@login_required(login_url='login')
def create_stripe_product(request): 
    form = PaymentProductForm()
    product = PaymentProduct.objects.all()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = PaymentProductForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = product
                post.save()
            return redirect('stripe-products')

    context = {'form': form}
    return render(request, 'payments/product_form.html', context)

@login_required(login_url='login')
def update_stripe_product(request, pk): 
    product = PaymentProduct.objects.get(id=pk)
    form = PaymentProductForm(instance=product)

    if request.method == 'POST':
        form = PaymentProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
        return redirect('intents')
    
    context = {'form': form, }
    return render(request, 'payments/product_form.html', context)

@login_required(login_url='login')
def delete_stripe_product(request, pk): 
    product = PaymentProduct.objects.get(id=pk)
    
    if request.method == 'POST':
        product.delete()
        return redirect('stripe-products')
 
    context = {'object': product}
    return render(request, 'delete_form.html', context)

##############################
####### Stripe Checkout ######
##############################
@method_decorator(login_required(login_url='login'), name='dispatch')
class PaymentsLandingPageView(TemplateView):
    template_name = 'payments/payments.html'

    def get_context_data(self, **kwargs):
        product = PaymentProduct.objects.all().first()
        context = super(PaymentsLandingPageView, self).get_context_data(**kwargs)
        context.update({
            'product': product,
            'STRIPE_PUBLIC_KEY': os.environ.get('STRIPE_PUBLIC_KEY'),
        })
        return context

@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = PaymentProduct.objects.get(id=product_id)
        YOUR_DOMAIN = os.environ.get('YOUR_DOMAIN')
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'eur',
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
                success_url= YOUR_DOMAIN + '/payments/success/',
                cancel_url= YOUR_DOMAIN + '/payments/cancel/',
            )
            if request.method == 'POST':
                return redirect(checkout_session.url, code=303)
            print(JsonResponse({
                'id': checkout_session.id
            }))
        except Exception as e:
            return str(e)
        
    
######################################
####### Stripe Payement Intents ######
######################################
@login_required(login_url='login')
def intentsLandingPage(request): 
    product = PaymentProduct.objects.all().first()
    publicKey = os.environ.get('STRIPE_PUBLIC_KEY')

    context = {'product': product, 'STRIPE_PUBLIC_KEY': publicKey}
    return render(request, 'payments/checkout.html', context)

@method_decorator(login_required(login_url='login'), name='dispatch')
class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
            try:
                product_id = self.kwargs['pk']
                product = PaymentProduct.objects.get(id=product_id)

                payment_intent = stripe.PaymentIntent.create(
                    amount=self.get_price_in_cents(),
                    currency='eur',
                    automatic_payment_methods = {'enabled': True},
                    metadata={
                        "product_id": product.id
                    }
                )
                return JsonResponse({
                    'clientSecret': payment_intent.client_secret
                })
            except Exception as e:
                return JsonResponse({'error': str(e) }) 
         

##############################
####### Stripe Webhooks ######
##############################
endpoint_secret = os.environ.get('WEBHOOK_SECRET')

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    
    if event['type'] == 'checkout.session.completed' or event['type'] == 'payment.intent.created':
        session = event['data']['object']

        customer_email = session['customer_details']['email']
        product_id = session['metadata']['product_id']

        product = PaymentProduct.objects.get(id=product_id)

        send_mail (
            subject = 'Here is your product',
            message = f'Thanks for your purchase, here is the product you ordered, find it here at {product.url}',
            recipient_list= [customer_email],
            from_email= [os.environ.get('EMAIL_HOST_USER')],
        )
    elif event['type'] == 'payment.intent.succeeded' or event['type'] == 'charge.succeeded':
        send_mail (
            subject = '💰💰💰 Payment Received!',
            message = f'You have received a payment of {product.price}',
            recipient_list= [os.environ.get('EMAIL_HOST_USER')],
            from_email= [os.environ.get('EMAIL_HOST_USER')],
        )
    else:
      print('Unhandled event type {}'.format(event['type']))
    
    return HttpResponse(status=200)
