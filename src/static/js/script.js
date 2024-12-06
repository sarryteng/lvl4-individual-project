const menuToggle = document.getElementById('menuToggle');
const overlayMenu = document.getElementById('overlayMenu');
const closeBtn = document.getElementById('closeBtn');

menuToggle.addEventListener('click', () => {
    overlayMenu.classList.add('show'); // Show the overlay menu
});

closeBtn.addEventListener('click', () => {
    overlayMenu.classList.remove('show'); // Hide the overlay menu
});
