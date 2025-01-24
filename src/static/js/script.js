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

document.addEventListener('DOMContentLoaded', () => {
    // Retrieve translatable strings from hidden divs in base.html
    const pleaseSelectMessage = document.getElementById('please-select-message').textContent.trim();
    const incorrectMessage = document.getElementById('incorrect-message').textContent.trim();
    const correctMessage = document.getElementById('correct-message').textContent.trim();
    const nextQuestionText = document.getElementById('next-question-text').textContent.trim();
    const quizCompletedMessage = document.getElementById('quiz-completed-message').textContent.trim();
    const scoreMessage = document.getElementById('score-message').textContent.trim();

    // Quiz functionality
    const quizContainer = document.getElementById('quiz-container');
    const questions = document.querySelectorAll('.quiz-question');
    const nextButton = document.getElementById('next-question');
    const quizSummary = document.getElementById('quiz-summary');
    let currentQuestionIndex = 0;
    let score = 0;

    quizContainer.addEventListener('click', (e) => {
        if (e.target.classList.contains('quiz-card')) {
            const selectedCard = e.target;
            const options = selectedCard.parentNode.querySelectorAll('.quiz-card');

            // Remove 'selected' class from all options in the current question
            options.forEach(card => card.classList.remove('selected'));

            // Add 'selected' class to the clicked option
            selectedCard.classList.add('selected');
        }
    });

    quizContainer.addEventListener('click', (e) => {
        if (e.target.classList.contains('check-answer')) {
            const currentQuestion = questions[currentQuestionIndex];
            const selectedCard = currentQuestion.querySelector('.quiz-card.selected');
            const resultDiv = currentQuestion.querySelector('.result');

            if (!selectedCard) {
                resultDiv.textContent = pleaseSelectMessage; // Use "Please select an answer." message
                return;
            }

            const correctAnswer = currentQuestion.dataset.correct;
            const allCards = currentQuestion.querySelectorAll('.quiz-card');

            // Highlight the correct answer in green
            allCards.forEach(card => {
                card.classList.add('disabled');
                if (card.dataset.answer === correctAnswer) {
                    card.classList.add('correct');
                }
            });

            if (selectedCard.dataset.answer === correctAnswer) {
                selectedCard.classList.add('selected');
                resultDiv.textContent = correctMessage; // Use "Correct!" message
                score++;
            } else {
                selectedCard.classList.add('incorrect');
                resultDiv.textContent = incorrectMessage.replace('{correctAnswer}', correctAnswer); // Replace placeholder with the correct answer
            }

            e.target.style.display = 'none'; // Hide the check button
            nextButton.style.display = currentQuestionIndex < questions.length - 1 ? 'block' : 'none';

            if (currentQuestionIndex === questions.length - 1) {
                displaySummary();
            }
        }
    });

    nextButton.addEventListener('click', () => {
        questions[currentQuestionIndex].style.display = 'none';
        currentQuestionIndex++;
        questions[currentQuestionIndex].style.display = 'block';

        // Update the URL with the current question index
        const baseURL = window.location.href.split('#')[0].split('?')[0];
        window.history.pushState(null, '', `${baseURL}#${currentQuestionIndex + 1}`);

        nextButton.style.display = 'none';
    });

    function displaySummary() {
        quizContainer.style.display = 'none';
        quizSummary.style.display = 'block';
        quizSummary.innerHTML = `
            <h3>${quizCompletedMessage}</h3>
            <p>${scoreMessage.replace('{score}', score).replace('{total}', questions.length)}</p>
            <ul>
                ${[...questions].map((q, i) => {
                    const correct = q.dataset.correct;
                    const selected = q.querySelector('.quiz-card.selected')?.dataset.answer;
                    const result = correct === selected ? correctMessage : incorrectMessage.replace('{correctAnswer}', correct);
                    return `<li>Question ${i + 1}: ${result}</li>`;
                }).join('')}
            </ul>
            <button id="restart-quiz" class="check-answer">${nextQuestionText}</button>
        `;

        // Add an event listener for the restart button
        document.getElementById('restart-quiz').addEventListener('click', restartQuiz);
    }

    function restartQuiz() {
        currentQuestionIndex = 0;
        score = 0;
        questions.forEach((question, index) => {
            question.style.display = index === 0 ? 'block' : 'none';
            const allCards = question.querySelectorAll('.quiz-card');
            allCards.forEach(card => {
                card.classList.remove('selected', 'correct', 'incorrect', 'disabled');
            });
            const resultDiv = question.querySelector('.result');
            resultDiv.textContent = '';
            question.querySelector('.check-answer').style.display = 'block';
        });

        quizContainer.style.display = 'block';
        quizSummary.style.display = 'none';
        nextButton.style.display = 'none';

        // Reset the URL to the first question
        const baseURL = window.location.href.split('#')[0].split('?')[0];
        window.history.pushState(null, '', `${baseURL}#1`);
    }
});

