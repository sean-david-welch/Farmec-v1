// Stripe Checkout // 
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
// Create an instance of the Stripe object with your publishable API key
var stripe = Stripe("{{ TEST_PUBLIC_KEY }}");
var checkoutButton = document.getElementById("checkout-button");
checkoutButton.addEventListener("click", function () {
  fetch("{% url 'create-checkout-session' product.id %}", {
    method: "POST",
    headers: {
        'X-CSRFToken': csrftoken
    }
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (session) {
      return stripe.redirectToCheckout({ sessionId: session.id });
    })
    .then(function (result) {
      // If redirectToCheckout fails due to a browser or network
      // error, you should display the localized error message to your
      // customer using error.message.
      if (result.error) {
        alert(result.error.message);
      }
    })
    .catch(function (error) {
      console.error("Error:", error);
    });
});