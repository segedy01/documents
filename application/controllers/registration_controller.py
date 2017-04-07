import json
from application.models.model import Users
from application import db


def create_user_controller(http_request):
    json_payload = http_request.json

    current_session = db.session

    if not json_payload:
        status = False
        msg = 'Please check Json Documentation or learn Json kungfu from a Json samurai'
        code = 415
        return status, msg, code
    try:
        name = json_payload.get('name')
        email = json_payload.get('email')
        password = json_payload.get('password')
        roles = "Admin"

        if email is None or password is None or name is None :
            status = False
            msg = 'Please Ensure all details are provided'
            code = 400
            return status, msg, code

        if Users.query.filter_by(email = email).first() is not None:
            status = False
            msg = 'User already exist. contact admin for more information'
            code = 400
            return status, msg, code

        user = Users(name = name, email = email, roles = roles)
        user.hash_password(password)
        current_session.add(user)
        current_session.commit()

        status = True
        msg = 'Registration Successful'
        code = 201
        return status, msg, code

    except Exception as e:
        print e
        status = False
        msg = 'Our servers are currently jammed. Give us a moment'
        code = 500
        return status, msg, code