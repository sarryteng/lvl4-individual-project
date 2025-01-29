// Menu toggle functionality
const menuToggle = document.getElementById('menuToggle');
const overlayMenu = document.getElementById('overlayMenu');
const closeBtn = document.getElementById('closeBtn');

menuToggle.addEventListener('click', () => {
    overlayMenu.classList.add('show'); // Show the overlay menu
});

closeBtn.addEventListener('click', () => {
    overlayMenu.classList.remove('show'); // Hide the overlay menu
});

// Language switcher functionality
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
        const currentParams = new URLSearchParams(window.location.search); // Get current URL parameters
        const questionParam = currentParams.get('question'); // Retrieve the current question index, if available

        // Construct the new path, preserving the `question` parameter
        const newPath = `/${lang}${window.location.pathname.substring(3)}${questionParam ? `?question=${questionParam}` : ''}`;
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

// Quiz functionality
document.addEventListener('DOMContentLoaded', () => {
    // Retrieve translatable strings from hidden divs in base.html
    const pleaseSelectMessage = document.getElementById('please-select-message').textContent.trim();
    const incorrectMessage = document.getElementById('incorrect-message').textContent.trim();
    const correctMessage = document.getElementById('correct-message').textContent.trim();
    const quizCompletedMessage = document.getElementById('quiz-completed-message').textContent.trim();
    const scoreMessage = document.getElementById('score-message').textContent.trim();
    const restartQuizText = document.getElementById('restart-quiz-text').textContent.trim(); 
    
    // Regex to match quiz URLs: /<lang>/learn/<concept>/quiz
    const quizURLPattern = /^\/(en|fr|es)\/learn\/[a-z_]+\/quiz$/;
    const currentPath = window.location.pathname;

    if (quizURLPattern.test(currentPath)) {
        const urlParams = new URLSearchParams(window.location.search);
        let currentQuestionIndex = parseInt(urlParams.get('question')) || 1; // Default to question=1 if not present
        const quizContainer = document.getElementById('quiz-container');
        const questions = document.querySelectorAll('.quiz-question');
        const nextButton = document.getElementById('next-question');
        const quizSummary = document.getElementById('quiz-summary');
        let score = 0;

        // Ensure the current question is displayed correctly based on the `question` parameter
        function showCurrentQuestion() {
            questions.forEach((question, index) => {
                question.style.display = index === (currentQuestionIndex - 1) ? 'block' : 'none';
            });
            nextButton.style.display = 'none'; // Always hide the Next button initially
        }

        // Display the current question based on the `question` parameter
        showCurrentQuestion();

        // Handle selecting an answer
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

        // Handle checking an answer
        quizContainer.addEventListener('click', (e) => {
            if (e.target.classList.contains('check-answer')) {
                const currentQuestion = questions[currentQuestionIndex - 1]; // Adjust for 1-based index
                const selectedCard = currentQuestion.querySelector('.quiz-card.selected');
                const resultDiv = currentQuestion.querySelector('.result');

                if (!selectedCard) {
                    resultDiv.textContent = pleaseSelectMessage; // Show "Please select an answer." message
                    return;
                }

                const correctAnswer = currentQuestion.dataset.correct;
                const allCards = currentQuestion.querySelectorAll('.quiz-card');

                // Highlight the correct answer in green and disable all answer options
                allCards.forEach(card => {
                    card.classList.add('disabled');
                    if (card.dataset.answer === correctAnswer) {
                        card.classList.add('correct');
                    }
                });

                if (selectedCard.dataset.answer === correctAnswer) {
                    selectedCard.classList.add('selected');
                    resultDiv.textContent = correctMessage; // Show "Correct!" message
                    score++;
                } else {
                    selectedCard.classList.add('incorrect');
                    resultDiv.textContent = incorrectMessage.replace('{correctAnswer}', correctAnswer); // Show correct answer
                }

                e.target.style.display = 'none'; // Hide the "Check" button
                nextButton.style.display = 'block'; // Show the "Next" button
            }
        });

        // Handle next question button
        nextButton.addEventListener('click', () => {
            // Check if it's the last question
            if (currentQuestionIndex < questions.length) {
                currentQuestionIndex++;

                // Update the URL with the current question index
                const newURL = `${window.location.pathname}?question=${currentQuestionIndex}`;
                window.history.pushState({ question: currentQuestionIndex }, "", newURL);

                showCurrentQuestion();
            } else {
                // If it's the last question, show the summary
                displaySummary();
            }
        });

        // Display the quiz summary at the end
        function displaySummary() {
            nextButton.style.display = 'none';
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
                <button id="restart-quiz" class="check-answer">${restartQuizText}</button>
            `;

            // Restart quiz button functionality
            document.getElementById('restart-quiz').addEventListener('click', restartQuiz);
        }
        
        // Restart quiz functionality
        function restartQuiz() {
            currentQuestionIndex = 1; // Reset to the first question
            score = 0;

            questions.forEach((question, index) => {
                question.style.display = index === 0 ? 'block' : 'none';
                question.querySelectorAll('.quiz-card').forEach(card => {
                    card.classList.remove('selected', 'correct', 'incorrect', 'disabled');
                });
                question.querySelector('.result').textContent = '';
                question.querySelector('.check-answer').style.display = 'block';
            });

            quizContainer.style.display = 'block';
            quizSummary.style.display = 'none';
            nextButton.style.display = 'none';

            // Reset the URL to the first question
            const baseURL = window.location.pathname;
            window.history.pushState({ question: 1 }, "", `${baseURL}?question=1`);
            showCurrentQuestion();
        }

        // Handle browser back/forward button navigation
        window.addEventListener('popstate', (event) => {
            if (event.state && event.state.question) {
                currentQuestionIndex = event.state.question;
                showCurrentQuestion();
            }
        });
    }    
});
