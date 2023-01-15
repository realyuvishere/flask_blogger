from flask import render_template, current_app as app, request, redirect, make_response, url_for
from ..controller import getUser, createUser, searchUsers, editUser, isFollowing, followUser, unfollowUser, getUserFollowingCount, getUserFollowersCount, getUserPostsCount, getUserPosts
from ..validator import ValidationError
from ..utils import custom_decrypt, tokenize, validToken, detokenize
from datetime import datetime

def authorizeUser(user, action):
    res = make_response(action())
    token = tokenize(user)
    res.set_cookie('token', token)
    return res

@app.route('/login', methods=['GET', 'POST'])
def login():
    m = request.method
    auth = request.cookies.get('token', None)

    if auth:
        if validToken(auth):
            return redirect(url_for('feed'))
        else:
            return redirect(url_for('logout'))

    
    def getLogin():
        return render_template('login.html')
    
    def postLogin():
        d = request.form
        user = getUser(username=d['username'])
        if (user):
            if custom_decrypt(string=user.password) == d['password']:
                return authorizeUser(user=user, action=lambda:redirect(url_for('feed')))
            else:
                return 'wrong password'
        else:
            return 'No user'

    return {
        'GET': getLogin,
        'POST': postLogin,
    }[m]()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    m = request.method
    auth = request.cookies.get('token', None)

    if auth:
        if validToken(auth):
            return redirect(url_for('feed'))
        else:
            return redirect(url_for('logout'))
    
    def getSignup():
        return render_template('signup.html')
    
    def postSignup():
        d = request.form
        data = {
            'username': d['username'],
            'name': d['name'],
            'password': d['password'],
            'email': d['email'],
        }
        user = createUser(data)
        if user:
            return authorizeUser(user=user, action=lambda:redirect(url_for('feed')))
        else:
            return render_template('signup.html', error={'message': 'something went wrong'})

    return {
        'GET': getSignup,
        'POST': postSignup,
    }[m]()

@app.route('/logout')
def logout():
    res = make_response(redirect(url_for('login')))
    res.delete_cookie('token')
    return res

@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    auth = request.cookies.get('token', None)

    if auth:
        if validToken(auth):
            pass
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('login'))
    
    data = getUser(username=username)
    uid = detokenize(auth)['id']
    fid = data.id

    return render_template('profile.html', 
        data=data, 
        showCTA=True, 
        following=bool(isFollowing(uid=uid, fid=fid)),
        ownprofile=(uid==fid),
        followers_count=getUserFollowersCount(uid=fid),
        following_count=getUserFollowingCount(uid=fid),
        posts_count=getUserPostsCount(uid=fid),
        posts=getUserPosts(uid=fid),
        showTime=datetime.fromtimestamp, 
    )

@app.route('/userprofile', methods=['GET', 'POST'])
def loggedUserProfile():
    auth = request.cookies.get('token', None)

    if auth:
        if validToken(auth):
            pass
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('login'))
    
    
    # username = detokenize(auth)['username']
    id = detokenize(auth)['id']

    if request.method == 'POST':
        d = request.form
        attrs = ['email', 'username', 'name']
        filtered_d = {
            'id': id
        }
        for att in attrs:
            filtered_d[att] = d[att]
        if editUser(filtered_d):
            pass
        else:
            return False
        
    data = getUser(id=id)

    return render_template('profile.html', 
        data=data, 
        edit=True, 
        showCTA=True,
        ownprofile=True,
        followers_count=getUserFollowersCount(uid=id),
        following_count=getUserFollowingCount(uid=id),
        posts_count=getUserPostsCount(uid=id),
        posts=getUserPosts(uid=id),
        showTime=datetime.fromtimestamp, 
        editing=True
    )

@app.route('/follow/<fid>', methods=['GET'])
def followUserPage(fid):
    auth = request.cookies.get('token', None)

    if auth:
        if validToken(auth):
            pass
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('login'))

    uid = detokenize(auth)['id']

    if isFollowing(uid=uid, fid=fid):
        if unfollowUser(uid=uid, fid=fid):
            return redirect(request.referrer)
    else:
        if followUser(uid=uid, fid=fid):
            return redirect(request.referrer)

@app.route('/searchuser', methods=['GET', 'POST'])
def searchUser():
    auth = request.cookies.get('token', None)
    
    if auth:
        if validToken(auth):
            pass
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('login'))
    username = request.form.get('searchbar')
    users = searchUsers(username=username)
    return render_template('searchedUsers.html', users=users)