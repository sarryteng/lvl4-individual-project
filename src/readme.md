# Cybersecurity Resource Hub

This project is a multilingual web application designed to educate users about cybersecurity, with a focus on mobile phone safety. It includes informative concepts, interactive quizzes, guides, and tools to help users better understand and apply cybersecurity best practices.

## File Structure

- **`app.py`**: The main entry point for the Flask application.
- **`config.py`**: Configuration settings for the application.
- **`wsgi.py`**: WSGI entry point for deploying the application.
- **`babel.cfg`**: Configuration file for Babel, used for managing translations.
- **`requirements.txt`**: Lists the Python dependencies required for the project.
- **`Procfile`**: Specifies the command to run the application on a platform like Heroku.
- **`manual.md`**: User manual for the project.
- **`backend/`**: Contains the backend logic, including views and URL routing.
  - **`views.py`**: Defines the routes and logic for rendering templates.
  - **`urls.py`**: (Optional) Could define URL patterns if used.
- **`static/`**: Contains static assets like CSS, JavaScript, and images.
  - **`css/`**: Stylesheets for the application.
  - **`js/`**: JavaScript files for interactive features.
  - **`images/`**: Images used in the application.
- **`templates/`**: HTML templates for the application.
  - Includes pages like `home.html`, `learn.html`, `tools.html`, and quiz templates.
- **`translations/`**: Contains translation files for multilingual support.
  - **`messages.pot`**: Template file for translations.
  - **`fr/`**: French translations.
- **`utils/`**: Utility scripts, such as `translate.py` for handling translations.
- **`tests/`**: Contains unit tests for the application.

## Build Instructions

### Requirements
To set up and run this project, you need the following:

- **Python 3.7 or higher**: The application is built using Python, so ensure you have the correct version installed.
- **Packages**: All required Python packages are listed in `requirements.txt`. These include:
  - Flask (3.0.3): For building the web application.
  - Flask-Babel (4.0.0): For multilingual support.
  - Babel (2.16.0): For managing translations.
  - Gunicorn (23.0.0): For deploying the application in production.
  - Deep-Translator (1.11.4): For handling translations.
  - And other dependencies listed in `requirements.txt`.

To install these dependencies, use the following command:
```bash
pip install -r [requirements.txt](http://_vscodecontentref_/0)
```

- **Operating System:** The project has been tested on macOS.   
- **Web Browser:** A web browser such as Google Chrome or Safari to access the application.  


### Build Steps
No building is required for this application. You can directly run the application using one of the following methods:

#### Option 1: Using `flask run`
1. Open a terminal and navigate to the `src` folder:
```bash
cd /path/to/lvl4-individual-project/src
```
2. Run the application using Flask:
```bash
flask run
```
3. Open your web browser and go to the URL provided in the terminal (usually http://127.0.0.1:5000).


#### Option 2: Using `python app.py`
1. Open a terminal and navigate to the `src` folder:
```bash
cd /path/to/lvl4-individual-project/src
```
2. Before running the application, ensure the port in `app.py` matches the desired port. By default, it is set to `5000`. Update the following line in `app.py` if needed:
```python
app.run(host="0.0.0.0", port=<desired_port>, debug=True)
```
3. Run the application:
```bash
python app.py
```
4. Open your web browser and go to: http://127.0.0.1:<desired_port>

Both methods will start the application, and you can access it in your browser.


## Test Steps
This section outlines the steps required to verify that the software functions correctly through both automated and manual testing.

### Automated Testing

Automated tests ensure core functionalities such as routing, language switching, and page accessibility work as expected.

#### Running Unit Tests

The unit tests are located in the `src/tests` directory. To execute all test cases, run the following command to execute the test suite:

```bash
python -m unittest discover -s src/tests
```
A successful run will output a summary indicating that all tests passed without errors.

### Manual Testing

Conduct manual testing to ensure the website is responsive across different devices, and to test other functionalities.

#### Steps for Manual Testing

1. **Responsiveness Testing**
- Open Google Chrome Developer Tools (`F12` or `Ctrl + Shift + I`).
- Use the responsive mode to simulate various screen sizes (e.g., smartphone, tablet, and desktop views).
- Verify that all elements adjust properly and remain accessible down to a width of **280px**.

2. **Quiz Functionality Testing**
- Start a quiz and verify that only one question is displayed at a time.
- Click the **Check** button after selecting an answer to confirm correct/incorrect responses are highlighted.
- Ensure the **Previous**, **Next**, and **Finish Quiz** buttons function correctly based on the question progression.
- Complete a quiz and verify that the summary reflects user answers and the correct score.
- Restart the quiz and ensure functionality resets properly.

3. **Language Switching Testing**
- Switch between English and French using the language selector.
- Verify that content is correctly translated.
- Check that special characters (%, $, etc.) render correctly in both languages.

#### Expected Outcome
- All pages should be accessible and display correct content.
- The website should be fully responsive across various screen sizes.
- The quiz should function correctly, with appropriate navigation and validation.
- The language switch should work seamlessly without breaking the UI or content.
