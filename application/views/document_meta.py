from application import app
from flask import jsonify, request
from application.controllers.document_meta_controller import create_document_data, delete_document_data

@app.route('/docsystem/createmeta', methods=["POST"])
def create_doc_meta():

    status, message, doc, code = create_document_data(request)
    return jsonify({"status": status, "message": message, "document identifier": doc}), code


@app.route('/docsystem/createmeta', methods=["DELETE"])
def delete_doc_meta():

    status, message, code = delete_document_data(request)
    return jsonify({"status": status, "message": message}), code
