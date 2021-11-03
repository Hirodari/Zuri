import os

# DEBUG = True

# SERVER_NAME = '127.0.0.1:5000'
SECRET_KEY = 'insecurekeyfordev'

# Flask-Mail.

MAIL_DEFAULT_SENDER = 'ADMIN <info@zurimaison.com>' 
MAIL_SERVER = 'mail.bvl.technology' #should match with MAIL_USERNAME
MAIL_PORT = 587 #465
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = os.environ['MAIL_USERNAME'] # Default sender should be different with MAIL_USERNAME
MAIL_PASSWORD = os.environ['MAIL_PASSWORD'] 
# set os variable ex: export MAIL_USERNAME=something@gmail.com
# or echo "export MAIL_PASSWORD=somepassword" >> .bashrc







