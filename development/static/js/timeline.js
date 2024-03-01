const left = document.querySelectorAll('.left-container, .right-container');

window.addEventListener('scroll', checkLeft);

checkLeft();

function checkLeft() {
    const triggerBottom = window.innerHeight / 5 * 4;

    left.forEach((left) => {
        const leftTop = left.getBoundingClientRect().top;

        if (leftTop < triggerBottom) {
            left.classList.add('show');
        }
    });
}