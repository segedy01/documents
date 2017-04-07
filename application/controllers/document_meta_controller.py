import json
from application.models.model import DocumentMetaData, Users, UsersDocuments
from application import db
from application.utils.utility import check_if_doc_exist, code_gen, valid_extension, verify_auth_token


def create_document_data(http_request):

    json_payload = http_request.json
    current_session = db.session

    if not json_payload:
        status = False
        doc = None
        msg = 'Please check Json Documentation or learn Json kungfu from a Json samurai'
        code = 415
        return status, msg, doc, code

    try:

        name = json_payload.get('name')
        doc_type = json_payload.get('type')

        if doc_type not in valid_extension:
            doc = None
            status = False
            msg = 'Please Check with Admin for valid extensions'
            code = 400
            return status, msg, doc, code

        if name is None:
            doc = None
            status = False
            msg = 'Please Ensure all details are provided'
            code = 400
            return status, msg, doc, code

        f_name = name.replace(' ', '')

        doc_string = code_gen(f_name)
        doc_name = (doc_string+f_name).lower()
        confirmed_doc_name = check_if_doc_exist(doc_name, name)
        doc_name_extension = confirmed_doc_name + '.' + doc_type

        document_data=DocumentMetaData(document_identifier=doc_name_extension, name=name)

        current_session.add(document_data)
        current_session.commit()

        status = True
        doc = confirmed_doc_name
        msg = 'Document Data Success'
        code = 201
        return status, msg, doc, code

    except Exception as e:

        print e
        doc = None
        status = False
        msg = 'Something went wrong. Contact admin for more information'
        code = 400
        return status, msg, doc, code


def delete_document_data(http_request):
    token = http_request.headers.get('X-Client-ID')
    des_token = verify_auth_token(token)

    email = des_token['token'].get('email')
    role = des_token['token'].get('role')

    current_session = db.session
    json_payload = http_request.json

    try:
        if not json_payload:
            status = False
            msg = 'Please check Json Documentation or learn Json kungfu from a Json samurai'
            code = 415
            return status, msg, code

        user = Users.query.filter_by(email=email).first()
        if not user or not role == 'User':
            status = False
            msg = 'Forbidden!!! You do not have the right for this'
            code = 415
            return status, msg, code

        document = json_payload.get('document')

        if document is None:
            status = False
            msg = 'Please Ensure all details are provided'
            code = 400
            return status, msg, code

        doc_assign = UsersDocuments.query.filter(UsersDocuments.document == document).all()
        document_data = DocumentMetaData.query.filter(DocumentMetaData.document_identifier == document).first()

        for records in doc_assign:
            current_session.delete(records)
        current_session.delete(document_data)
        current_session.commit()

        status = True
        msg = 'Document Delete Success'
        code = 201
        return status, msg, code

    except Exception as e:

        print e
        status = False
        msg = 'Something went wrong. Contact admin for more information'
        code = 400
        return status, msg, code
