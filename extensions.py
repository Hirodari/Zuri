from flask_mail import Mail

from flask_wtf.csrf import CSRFProtect
# pip install Flask_Mail
# pip install flask_wtf

mail = Mail()
csrf = CSRFProtect()