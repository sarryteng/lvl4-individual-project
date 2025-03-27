# Cybersecurity Resource Hub

This project is a multilingual web application designed to educate users about cybersecurity, with a focus on mobile phone safety. It includes interactive quizzes, guides, and tools to help users understand and apply cybersecurity best practices.

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

List the all of the pre-requisites software required to set up your project (e.g. compilers, packages, libraries, OS, hardware)

For example:

* Python 3.7
* Packages: listed in `requirements.txt` 
* Tested on Windows 10

or another example:

* Requires Raspberry Pi 3 
* a Linux host machine with the `arm-none-eabi` toolchain (at least version `x.xx`) installed
* a working LuaJIT installation > 2.1.0

### Build steps

List the steps required to build software. 

Hopefully something simple like `pip install -e .` or `make` or `cd build; cmake ..`. In
some cases you may have much more involved setup required.

### Test steps

List steps needed to show your software works. This might be running a test suite, or just starting the program; but something that could be used to verify your code is working correctly.

Examples:

* Run automated tests by running `pytest`
* Start the software by running `bin/editor.exe` and opening the file `examples/example_01.bin`


To set up and run this project, you need the following:

- Python 3.7 or higher
- Packages listed in `requirements.txt`
- A web browser for accessing the application
- (Optional) A platform like Heroku for deployment

### Build Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd lvl4-individual-project/src