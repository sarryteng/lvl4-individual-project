class Config:
    TESTING = False
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_TRANSLATION_DIRECTORIES = 'translations'

class TestConfig(Config):
    TESTING = True