from application import app
from flask import jsonify, request
from application.controllers.login_controller import verify_password

@app.route('/docsystem/login', methods=["POST"])
def login():

    status, message, token, code = verify_password(request)
    return jsonify({"status": status, "message": message, "token": token}), code