from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return f'{self.firstname} {self.lastname}'
    
    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname
        }