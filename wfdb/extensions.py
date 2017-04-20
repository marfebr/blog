from flask_login import LoginManager
from flask_bcrypt import Bcrypt

#from wfdb.models import User

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.session_protection='strong'
login_manager.login_view = 'main.login'

#def load_user(userid):
#    return User.query.get(userid)
