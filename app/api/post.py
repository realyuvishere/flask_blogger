from flask_restful import Resource, fields, marshal_with, reqparse

from ..validator import ValidationError, NotFoundError
from ..models import User
from ..config import db

create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument('username')
create_user_parser.add_argument('email')

update_user_parser = reqparse.RequestParser()
update_user_parser.add_argument('email')

resource_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String
}

class PostAPI(Resource):
    @marshal_with(resource_fields)
    def get(self, username):
        user = db.session.query(User).filter(User.username == username).first()
        if user is None:
            raise NotFoundError(status_code=404)
        return user

    def put(self, username):
        args = update_user_parser.parse_args()
        return {
            'hello': 'world'
        }

    @marshal_with(resource_fields)
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

    def delete(self):
        # print(id)
        return {
            'hello': 'world'
        }

class PostLikeAPI(Resource):
    @marshal_with(resource_fields)
    def get(self, username):
        user = db.session.query(User).filter(User.username == username).first()
        if user is None:
            raise NotFoundError(status_code=404)
        return user

    # @marshal_with(resource_fields)
    # def post(self):
    #     args = create_user_parser.parse_args()
    #     username = args.get("username", None)
    #     email = args.get("email", None)
    #     password = args.get("password", None)

    #     if username is None:
    #         raise ValidationError(error_message="Username is required")

    #     if email is None:
    #         raise ValidationError(error_message="Email is required")

    #     if "@" in email:
    #         pass
    #     else:
    #         raise ValidationError(error_message="Invalid email")

    #     user = db.session.query(User).filter((User.username == username) | (User.email == email)).first()
        
    #     if user:
    #         raise ValidationError(error_message="Duplicate user")

    #     new_user = User(username=username, email=email, password=password)
    #     db.session.add(new_user)
    #     db.session.commit()
    #     return new_user

    # def delete(self, id):
    #     print(id)
    #     return {
    #         'hello': 'world'
    #     }
