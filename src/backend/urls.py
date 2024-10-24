from .views import home, learn, guides, tools

def register_routes(app):
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/learn', 'learn', learn)
    app.add_url_rule('/guides', 'guides', guides)
    app.add_url_rule('/tools', 'tools', tools)
