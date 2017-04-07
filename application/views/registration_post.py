from application import app
from flask import jsonify, request
from application.controllers.registration_controller import create_user_controller

@app.route('/docsystem/create', methods=["POST"])
def create_user():

    status, message, code = create_user_controller(request)
    return jsonify({"status": status, "message": message}), code
