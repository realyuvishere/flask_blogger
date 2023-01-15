from ..models.User import User
# from ..validator import ValidationError
from ..config import db
from ..utils import custom_encrypt



def searchUsers(username=''):
    users = User.query.filter(User.username.contains(username)).all()
    return users

def createUser(data={}):
    if getUser(data['username']):
        return None
    else:
        try:
            new_user = User(
                username=data['username'], 
                email=data['email'], 
                name=data['name'], 
                password=custom_encrypt(string=data['password'])
            )
            db.session.add(new_user)
        except:
            db.session.rollback()
            raise Exception('DB error.')
        else:
            db.session.commit()
            return new_user

def deleteUser(uid=''):
    User.query.filter_by(id=uid).delete()
    db.session.commit()
    return True

def editUser(data={}):
    try:
        user = getUser(id=data['id'])
        del data['id']
        for key in data:
            setattr(user, key, data[key])
        
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return True


def getUser(id='', username=''):
    user = db.session.query(User).filter((User.id == id) | (User.username == username)).first()
    return user

