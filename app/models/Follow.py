from ..config import db

class Follow(db.Model):
    __tablename__='follows'
    follower_id=db.Column(db.Integer, primary_key=True, nullable=False)
    following_id=db.Column(db.Integer, primary_key=True, nullable=False)