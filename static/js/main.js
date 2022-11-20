// const navbar = document.getElementById('navbar');
// let scrolled = false;

// window.onscroll = function() {
//     if (window.scrollY > 550) {
//         navbar.classList.remove('top');
//         if (!scrolled) {
//             navbar.style.transform = 'translateY(-10px)';
//         }
//         setTimeout(function() {
//             navbar.style.transform = 'translateY(0)';
//             scrolled = true;
//         }, 300)
//     } else {
//         navbar.classList.add('top');
//         scrolled = false;
//     }
// }

// Smooth Scrolling
$('#navbar a, .btn').on('click', function (e) {
    if (this.hash !== '') {
        e.preventDefault();

        const hash = this.hash;

        $('html, body').animate(
            {
                scrollTop: $(hash).offset().top - 60,
            },
            1000
        );
    }
});

// To top button
const toTop = document.querySelector("to-top");

window.addEventListener("scroll", () => {
    if (window.scrollY < 100) {
        toTop.classList.remove("active");
    }
})