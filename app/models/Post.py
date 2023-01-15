from ..config import db

class Post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    # Add foreign key relation here
    author=db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title=db.Column(db.String, nullable=False)
    content=db.Column(db.String, nullable=False)
    timestamp=db.Column(db.Integer, nullable=False)
    media=db.Column(db.String)