from django.urls import path
from . views import PaymentsLandingPageView, SucessView, CancelView, StripeIntentView, IntentsLandingPageView
from . views import CreateCheckoutSessionView
from . import views

urlpatterns = [
    path('intents/', IntentsLandingPageView.as_view(), name='intents'),
    path('payment-product/<pk>/', IntentsLandingPageView.as_view(), name='payment-product'),
    path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),

    path('webhooks/stripe/', views.stripe_webhook, name='stripe-webhook'),

    path('payments/', PaymentsLandingPageView.as_view(), name='payments'),
    path('success/', SucessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]