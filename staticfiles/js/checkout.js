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
    },
  }).then(r => r.json())

  const appearance = {
    theme: 'night',
  };

  const elements = stripe.elements({appearance, clientSecret})
  const linkAuthenticationElement = elements.create("linkAuthentication");
  linkAuthenticationElement.mount("#link-authentication-element");

  linkAuthenticationElement.on('change', (event) => {
    emailAddress = event.value.email;
  });

  const paymentElementOptions = {
    layout: "tabs",
  };
  
  const paymentElement = elements.create('payment', paymentElementOptions)
  paymentElement.mount('#payment-element')

  const form = document.getElementById('payment-form')
  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const {error} = await stripe.confirmPayment({
      elements,
      confirmParams: {
        return_url: "http://127.0.0.1:8000/stripepayments/success/",
        receipt_email: emailAddress,
      }
    })
    if(error) {
      const messages = document.getElementById('error-messages')
      messages.innerText - error.message;
    }
  })
})

function showMessage(messageText) {
  const messageContainer = document.querySelector("#payment-message");

  messageContainer.classList.remove("hidden");
  messageContainer.textContent = messageText;

  setTimeout(function () {
    messageContainer.classList.add("hidden");
    messageText.textContent = "";
  }, 4000);
};

// Show a spinner on payment submission
function setLoading(isLoading) {
  if (isLoading) {
    // Disable the button and show a spinner
    document.querySelector("#submit").disabled = true;
    document.querySelector("#spinner").classList.remove("hidden");
    document.querySelector("#button-text").classList.add("hidden");
  } else {
    document.querySelector("#submit").disabled = false;
    document.querySelector("#spinner").classList.add("hidden");
    document.querySelector("#button-text").classList.remove("hidden");
  }
};