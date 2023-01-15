from flask_restful import Resource, fields, marshal_with, reqparse

from ..validator import ValidationError, NotFoundError
from ..models.User import User
from ..config.db import db
from ..controller.user import getUser, createUser

create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument('username')
create_user_parser.add_argument('email')
create_user_parser.add_argument('name')
create_user_parser.add_argument('id')
create_user_parser.add_argument('password')

update_user_parser = reqparse.RequestParser()
update_user_parser.add_argument('email')
update_user_parser.add_argument('name')
update_user_parser.add_argument('username')
update_user_parser.add_argument('id')

class UserMarshals:
    normalised = {
        'id': fields.Integer,
        'username': fields.String,
        'email': fields.String,
        'name': fields.String,
    }

class UserLoginAPI(Resource):
    @marshal_with(UserMarshals.normalised)
    def post(self):
        args = create_user_parser.parse_args()
        username = args.get("username", None)
        email = args.get("email", None)
        password = args.get("password", None)

        if username is None:
            raise ValidationError(error_message="Username is required")

        if email is None:
            raise ValidationError(error_message="Email is required")

        if "@" in email:
            pass
        else:
            raise ValidationError(error_message="Invalid email")

        user = db.session.query(User).filter((User.username == username) | (User.email == email)).first()
        
        if user:
            raise ValidationError(error_message="Duplicate user")

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

class UserSignupAPI(Resource):
    @marshal_with(UserMarshals.normalised)
    def post(self):
        args = create_user_parser.parse_args()
        username = args.get("username", None)
        email = args.get("email", None)
        password = args.get("password", None)

        if username is None:
            raise ValidationError(error_message="Username is required")

        if email is None:
            raise ValidationError(error_message="Email is required")

        if "@" in email:
            pass
        else:
            raise ValidationError(error_message="Invalid email")

        user = db.session.query(User).filter((User.username == username) | (User.email == email)).first()
        
        if user:
            raise ValidationError(error_message="Duplicate user")

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

class UserProfileAPI(Resource):
    @marshal_with(UserMarshals.normalised)
    def get(self, username):
        user = getUser(username=username)
        if user:
            return user
        else:
            raise NotFoundError(error_message='User not found.')

    @marshal_with(UserMarshals.normalised)
    def post(self):
        args = create_user_parser.parse_args()
        username = args.get("username", None)
        email = args.get("email", None)
        name = args.get("name", None)
        password = args.get("password", None)

        if not username:
            raise ValidationError(error_message="Username is required")

        if not email:
            raise ValidationError(error_message="Email is required")

        if "@" in email:
            pass
        else:
            raise ValidationError(error_message="Invalid email")

        user = getUser(username=username)
        
        if user:
            raise ValidationError(error_message="Duplicate user")

        new_user = createUser({'email': email, 'name': name, 'username': username})
        return new_user