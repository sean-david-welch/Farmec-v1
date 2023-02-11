const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

document.addEventListener('DOMContentLoaded', async () => {
  // Fetch Publishable Key and init stripe
  // const {publishableKey} = await fetch('/stripepayments/intents/').then(r => r.json())
  const stripe = Stripe("pk_test_51MXRDIF4Np2hFMT0RIQLnmkUzb0FKSVHnxXhKt2N35xfkoptA8B8DyC8cOEZ2Ywok4kBZCQ1cVmjanaehEdKPfZY00tg4vjBjn")


  // Fetch client secret and init elements
  const {clientSecret} = await fetch("/stripepayments/create-payment-intent/1/", {
    method: "POST",
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    }
  }).then(r => r.json())


  const elements = stripe.elements({clientSecret})
  const paymentElement = elements.create('payment')
  paymentElement.mount('#payment-element')

  const form = document.getElementById('payment-form')
  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const {error} = await stripe.confirmPayment({
      elements,
      confirmParams: {
        return_url: "http://127.0.0.1:8000/stripepayments/success/",

      }
    })
    if(error) {
      const messages = document.getElementById('error-messages')
      messages.innerText - error.message;
    }
  })
})