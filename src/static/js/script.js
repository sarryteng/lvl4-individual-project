const menuToggle = document.getElementById('menuToggle');
const overlayMenu = document.getElementById('overlayMenu');
const closeBtn = document.getElementById('closeBtn');

menuToggle.addEventListener('click', () => {
    overlayMenu.classList.add('show'); // Show the overlay menu
});

closeBtn.addEventListener('click', () => {
    overlayMenu.classList.remove('show'); // Hide the overlay menu
});

const languageSwitcher = document.querySelector('.language-switcher');
const languageDropdown = document.getElementById('languageDropdown');
const currentLanguage = document.getElementById('currentLanguage');

// Toggle the visibility of the dropdown menu on click
languageSwitcher.addEventListener('click', () => {
    languageDropdown.classList.toggle('show'); // Toggle dropdown visibility
    updateDropdown(); // Ensure dropdown is updated every time it's toggled
});

// Hide the dropdown when clicking outside of it
document.addEventListener('click', (event) => {
    if (!languageSwitcher.contains(event.target) && !languageDropdown.contains(event.target)) {
        languageDropdown.classList.remove('show'); // Hide dropdown
    }
});

// Change the current language abbreviation dynamically and redirect
const languageLinks = languageDropdown.querySelectorAll('a');
languageLinks.forEach(link => {
    link.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent default link behavior
        const lang = event.target.getAttribute('data-lang'); // Get the selected language code
        const newPath = `/${lang}${window.location.pathname.substring(3)}`; // Update the URL
        window.location.href = newPath; // Redirect to the new language-specific path
    });
});

// Function to update the dropdown and exclude the current language
function updateDropdown() {
    const currentLang = currentLanguage.textContent.toLowerCase(); // Get the current language abbreviation
    const allLinks = languageDropdown.querySelectorAll('a');
    
    allLinks.forEach(link => {
        const linkLang = link.getAttribute('data-lang');
        if (linkLang === currentLang) {
            link.style.display = 'none'; // Hide the current language
        } else {
            link.style.display = 'block'; // Show the other languages
        }
    });
}

// Initially exclude the current language from the dropdown
updateDropdown();
