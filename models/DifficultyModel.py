from config import db

class Difficulty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    # relasi dengan tabel machine
    machine = db.relationship('Machine', backref='difficulty', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }