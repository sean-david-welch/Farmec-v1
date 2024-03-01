document.addEventListener("DOMContentLoaded", async () => {
    // const {publishableKey} = await fetch("/config").then(r => r.json())
    const stripe = Stripe("pk_test_51MXRDIF4Np2hFMT0RIQLnmkUzb0FKSVHnxXhKt2N35xfkoptA8B8DyC8cOEZ2Ywok4kBZCQ1cVmjanaehEdKPfZY00tg4vjBjn")

    const params = new URLSearchParams(window.location.href)
    const clientSecret = params.get('payment_intent_client_secret')

    const {paymentIntent} = await stripe.retrievePaymentIntent(clientSecret)
    const paymentIntentPre = document.getElementById('payment-intent')
    paymentIntentPre.innerText = JSON.stringify(paymentIntent, null, 2)
})