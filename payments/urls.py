from django.urls import path
from . views import PaymentsLandingPageView, StripeIntentView
from . views import CreateCheckoutSessionView
from . import views

urlpatterns = [
    path('success/', views.successview, name='success'),
    path('cancel/', views.cancelview, name='cancel'),

    path('intents/', views.intentsLandingPage, name='intents'),
    path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    
    path('payments/', PaymentsLandingPageView.as_view(), name='payments'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),

    path('webhooks/stripe/', views.stripe_webhook, name='stripe-webhook'),

    path('stripe-products/', views.stripe_products, name='stripe-products'),
    path('create-stripe-product/', views.create_stripe_product, name='create-stripe-product'),
    path('update-stripe-product/<pk>/', views.update_stripe_product, name='update-stripe-product'),
    path('delete-stripe-product/<pk>/', views.delete_stripe_product, name='delete-stripe-product')

]