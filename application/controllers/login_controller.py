import json
from application.models.model import Users
from application import db
from application.utils.utility import *


def verify_password(http_request):

    json_payload = http_request.json
    try:
        if not json_payload:
            token = None
            status = False
            msg = 'Please check Json Documentation or learn Json kungfu from a Json samurai'
            code = 415
            return status, msg, token, code

        email = json_payload.get('email')
        password = json_payload.get('password')

        user = Users.query.filter_by(email=email).first()
        if not user or not user.verify_password(password):
            token = None
            status = False
            msg = 'You cant beat the system.'
            code = 401
            return status, msg, token, code
        tokenize = {
            "email": user.email,
            "role": user.roles
        }

        token = generate_auth_token(tokenize)
        status = True
        msg = 'Success.'
        code = 200
        return status, msg, token, code


    except Exception as e:
        print e
        token = None
        status = False
        msg = 'Our servers are currently jammed. Give us a moment'
        code = 500
        return status, msg, token, code
