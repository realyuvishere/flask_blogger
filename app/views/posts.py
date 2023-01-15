from flask import render_template, request, redirect, url_for, current_app as app
from ..utils import validToken, detokenize
from ..controller import createPost, editPost, deletePost, getPost, fetchPosts, isLiked, getComments, getPostLikes, likePost, unlikePost
import time
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def feed():
    auth = request.cookies.get('token', None)

    if auth:
        if validToken(auth):
            pass
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('login'))

    posts = fetchPosts()

    return render_template('feed.html', showCTA=True, posts=posts, showTime=datetime.fromtimestamp)

@app.route('/post/<pid>')
def viewPost(pid):
    auth = request.cookies.get('token', None)

    if auth:
        if validToken(auth):
            pass
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('login'))
    
    post = getPost(post_id=pid)

    return render_template('post.html', 
        post=post['post'], 
        author=post['author'], 
        showTime=datetime.fromtimestamp, 
        liked=isLiked(pid=pid, uid=detokenize(token=auth)['id']),
        comments=getComments(pid=pid),
        likeCount=getPostLikes(pid=pid),
    )

@app.route('/post/create', methods=['POST'])
def newPostPage():
    auth = request.cookies.get('token', None)

    if auth:
        if validToken(auth):
            pass
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('login'))

    d = request.form
    fd = {
        'title': d['blog_title'],
        'content': d['blog_content'],
        'author': detokenize(token=auth)['id'],
        'timestamp': time.time_ns()
    }
    if createPost(fd):
        return redirect(request.referrer)
    else:
        return False


@app.route('/post/edit', methods=['POST'])
def editPostPage():
    auth = request.cookies.get('token', None)
    
    if auth:
        if validToken(auth):
            pass
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('login'))
    
    return redirect(request.referrer)


@app.route('/post/delete/<pid>', methods=['GET'])
def deletePostPage(pid):
    auth = request.cookies.get('token', None)

    if auth:
        if validToken(auth):
            pass
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('login'))
    
    return redirect(request.referrer)

@app.route('/post/like/<pid>', methods=['GET'])
def likePostPage(pid):
    auth = request.cookies.get('token', None)

    if auth:
        if validToken(auth):
            pass
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('login'))
    
    uid = detokenize(token=auth)['id']
    if isLiked(pid=pid, uid=uid):
        if unlikePost(pid=pid, uid=uid):
            return redirect(request.referrer)
    else:
        if likePost(pid=pid, uid=uid):
            return redirect(request.referrer)

@app.route('/post/comment', methods=['POST'])
def commentPostPage():
    auth = request.cookies.get('token', None)

    if auth:
        if validToken(auth):
            pass
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('login'))

    
    return redirect(request.referrer)

