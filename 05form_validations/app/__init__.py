from flask import Flask



app = Flask(__name__)
RC_SITE_KEY = "6LfvibwUAAAAACU40hRo6G9yYv86F4FG2wU73N9X"
RC_SECRET_KEY = "6LfvibwUAAAAADoiSCUCzmUuGMgqj4Jmjcy_J0Pb"



app.config['SECRET_KEY']="herdtohacksecretkey"
app.config['RECAPTCHA_PUBLIC_KEY']= RC_SITE_KEY
app.config['RECAPTCHA_PRIVATE_KEY']= RC_SECRET_KEY


from app.views import *
from app.views import *