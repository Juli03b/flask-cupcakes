from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DEFAULT_IMG = 'https://tinyurl.com/demo-cupcake'

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, nullable=False, default=DEFAULT_IMG)

    def __repr__(self):
        return f'<Cupcake {self.id} {self.flavor} {self.size} {self.rating}>'

    def serialize(self):
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }