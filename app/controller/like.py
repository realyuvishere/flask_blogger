from ..models.Like import Like
from ..config.db import db

def likePost(pid, uid):
    try:
        like = Like(
            post_id=pid,
            user_id=uid
        )
        db.session.add(like)
    except:
        db.session.rollback()
        raise Exception('DB Error.')
    else:
        db.session.commit()
        return like

def unlikePost(pid, uid):
    Like.query.filter_by(post_id=pid, user_id=uid).delete()
    db.session.commit()
    return True

def getPostLikes(pid):
    likes = Like.query.filter_by(post_id=pid).count()
    return likes

def isLiked(pid, uid):
    like = Like.query.filter_by(post_id=pid, user_id=uid).first()
    return like