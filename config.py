from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# init app & db connect
app = Flask(__name__)

# Konfigurasi MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://learnflaskapiuts_zulunicego:b0406f6eaa7838b395266a384309d56eba4f9e95@0ug9z.h.filess.io/learnflaskapiuts_zulunicego'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()
