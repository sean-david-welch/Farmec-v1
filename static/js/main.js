// To top button
const toTop = document.querySelector("to-top");

window.addEventListener("scroll", () => {
    if (window.scrollY < 100) {
        toTop.classList.remove("active");
    }
});