from config import app, db
from routes.Machine_bp import machine_bp
from routes.Category_bp import category_bp
from routes.Difficulty_bp import difficulty_bp


app.register_blueprint(machine_bp)
app.register_blueprint(category_bp)
app.register_blueprint(difficulty_bp)

@app.route("/")
def home():
    return "MACHINES CTF API"

db.create_all()
# uncomment this if want deploy locally
# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)
