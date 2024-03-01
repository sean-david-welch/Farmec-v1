const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navList = document.getElementsByClassName('nav-list')[0]
const navColor = document.getElementById('navbar')

toggleButton.addEventListener('click', () => {
    navList.classList.toggle('mobile')
    navColor.classList.toggle('mobile')
})