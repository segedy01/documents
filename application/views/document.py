from application import app
from flask import jsonify, request
from application.controllers.document_controller import post_document

@app.route('/docsystem/<document_identity>/upload', methods=["POST"])
def upload_file(document_identity):

    status, message, code = post_document(request, document_identity)
    return jsonify({"status": status, "message": message}), code