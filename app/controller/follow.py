from ..models.Follow import Follow
from ..config import db

def followUser(uid, fid):
    try:
        follow = Follow(
            follower_id=uid,
            following_id=fid
        )
        db.session.add(follow)
    except:
        db.session.rollback()
        raise Exception('DB Error.')
    else:
        db.session.commit()
        return follow

def unfollowUser(uid, fid):
    Follow.query.filter_by(follower_id=uid, following_id=fid).delete()
    db.session.commit()
    return True

def getUserFollowersCount(uid):
    followers = Follow.query.filter_by(following_id=uid).count()
    return followers

def getUserFollowingCount(uid):
    following = Follow.query.filter_by(follower_id=uid).count()
    return following

def isFollowing(uid, fid):
    follow = Follow.query.filter_by(following_id=fid, follower_id=uid).first()
    return follow