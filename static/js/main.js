// To top button
const toTop = document.querySelector("to-top");

window.addEventListener("scroll", () => {
    if (window.scrollY < 100) {
        toTop.classList.remove("active");
    }
})

// Smooth Scrolling
$('#navbar a, .btn').on('click', function (e) {
    if (this.hash !== '') {
        e.preventDefault();

        const hash = this.hash;

        $('html, body').animate(
            {
                scrollTop: $(hash).offset().top - 100,
            },
            1000
        );
    }
});
