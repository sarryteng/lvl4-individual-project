const menuToggle = document.getElementById('menuToggle');
const overlayMenu = document.getElementById('overlayMenu');
const closeBtn = document.getElementById('closeBtn');

menuToggle.addEventListener('click', () => {
    overlayMenu.style.display = 'block'; // Show the overlay menu
});

closeBtn.addEventListener('click', () => {
    overlayMenu.style.display = 'none'; // Hide the overlay menu
});

// Close the overlay if clicked outside the menu
overlayMenu.addEventListener('click', (event) => {
    if (event.target === overlayMenu) {
        overlayMenu.style.display = 'none'; // Hide the overlay if clicked outside
    }
});
