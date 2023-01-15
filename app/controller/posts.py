from ..models.Post import Post
from ..config.db import db
from .user import getUser

def createPost(data={}):
    try:
        post = Post(
            title=data['title'], 
            content=data['content'], 
            author=data['author'], 
            timestamp=data['timestamp']
        )
        db.session.add(post)
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return post

def editPost(data={}):
    try:
        post = getPost(id=data['id'])['post']
        del data['id']
        for key in data:
            setattr(post, key, data[key])
        
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return True

def deletePost(pid):
    Post.query.filter_by(d=pid).delete()
    db.session.commit()
    return True

def getPost(post_id):
    post = Post.query.get(post_id)
    author = getUser(id=post.id)
    return {
        'post': post,
        'author': author,
    }

def getUserPosts(uid):
    posts = Post.query.filter_by(author=uid).all()
    return posts

def getUserPostsCount(uid):
    count = Post.query.filter_by(author=uid).count()
    return count

def fetchPosts():
    p = Post.query.all()
    posts = []
    for post in p:
        author = getUser(id=post.author)
        posts.append({'post': post, 'author': author})
    
    return posts