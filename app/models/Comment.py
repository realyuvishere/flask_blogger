from ..config import db

class Comment(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True, unique=True)
    content=db.Column(db.String, nullable=False)
    author=db.Column(db.Integer, nullable=False)
    post=db.Column(db.Integer, nullable=False)