from application import app
from flask import jsonify, request
from application.controllers.assign_document_controller import *


@app.route('/docsystem/assigner', methods=["POST"])
def assign_doc():

    status, message, code = create_assign(request)
    return jsonify({"status": status, "message": message}), code


@app.route('/docsystem/assigner', methods=["GET"])
def view_doc():

    status, message, data, code = view_assigned_document(request)
    return jsonify({"status": status, "message": message, "Documents": data}), code


@app.route('/docsystem/assigner', methods=['DELETE'])
def delete_doc():

    status, message, code = delete_document(request)
    return jsonify({"status": status, "message": message}), code


@app.route('/docsystem/assigner', methods=['PATCH'])
def patch_doc():

    status, message, code = patch_assign_doc(request)
    return jsonify({"status": status, "message": message}), code


@app.route('/docsystem/<document>/status', methods=['GET'])
def check_status(document):

    status, message, data, code = view_doc_status(request, document)
    return jsonify({"status": status, "message": message, "data": data}), code