from flask import Flask
from views.zuri import page
from extensions import mail, csrf
from flask_mail import Mail

# app = Flask(__name__)



def create_app(settings_override=None):
    
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(page)
    
    extensions(app)

    return app

def extensions(app):
    
    mail.init_app(app)
    csrf.init_app(app)

    return None

app = create_app()

if __name__ == '__main__':
	# app.run(debug=True)
	app.run(host='0.0.0.0', port=5000)