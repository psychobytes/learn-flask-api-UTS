from config import db

class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    # foreign key ke tabel category
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    # foreign key ke tabel difficulty
    difficulty_id = db.Column(db.Integer, db.ForeignKey('difficulty.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'category_id' : self.category_id,
            'difficulty_id' : self.difficulty_id
        }
