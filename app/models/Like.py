from ..config import db

class Like(db.Model):
    __tablename__='likes'
    post_id=db.Column(db.Integer, nullable=False, primary_key=True)
    user_id=db.Column(db.Integer, nullable=False, primary_key=True)