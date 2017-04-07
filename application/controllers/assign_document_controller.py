import json
from application import app
from application.models.model import Users, DocumentMetaData, UsersDocuments
from application import db
from application.utils.utility import *
import os


def create_assign(http_request):

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
        if not user or not role == 'Admin':
            status = False
            msg = 'Forbidden!!! You do not have the right for this'
            code = 415
            return status, msg, code

        document = json_payload.get('document')
        email = json_payload.get('email')

        doc_exist = DocumentMetaData.query.filter_by(document_identifier=document).first()
        email_exist =  Users.query.filter_by(email=email).first()
        if not doc_exist or not email_exist:
            status = False
            msg = 'Email or Document does not exist'
            code = 415
            return status, msg, code
        user = UsersDocuments.query.filter(UsersDocuments.document == document, UsersDocuments.email == email).first()
        if user:
            status = False
            msg = 'Document has been Assigned already. Try another document.'
            code = 415
            return status, msg, code
        assigned = UsersDocuments(document=document, email=email)

        current_session.add(assigned)
        current_session.commit()

        status = True
        msg = 'Document Assigned Successfully'
        code = 200
        return status, msg, code


    except Exception as e:
        print e
        status = False
        msg = 'Our Servers Are currently busy, Try again later '
        code = 500
        return status, msg, code


def view_assigned_document(http_request):
    token = http_request.headers.get('X-Client-ID')
    des_token = verify_auth_token(token)
    print des_token

    email = des_token['token'].get('email')

    user = Users.query.filter_by(email=email).first()
    if not user:
        status = False
        msg = 'Forbidden!!! You do not have the right for this'
        code = 415
        data = ''
        return status, msg, data, code

    try:
        user_docs = UsersDocuments.query.filter_by(email=email)
        document_list = []
        for docs in user_docs:
            doc_dict ={}
            document = DocumentMetaData.query.filter_by(document_identifier=docs.document).first()
            doc_dict['Document Path'] = os.path.join(app.config['UPLOAD_FOLDER'], document.document_identifier)
            doc_dict['Name'] = document.name
            doc_dict['Create Date'] = document.Date
            document_list.append(doc_dict)

        status = True
        msg = 'Success'
        code = 200
        data = document_list
        return status, msg, data, code

    except Exception as e:
        print e
        status = 'error'
        msg = 'error in connection'
        code = 500
        data = ''
        return msg, status, data, code


def delete_assign_doc(http_request):
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
        email = json_payload.get('email')

        doc_exist = DocumentMetaData.query.filter_by(document_identifier=document).first()
        email_exist = Users.query.filter_by(email=email).first()
        if not doc_exist or not email_exist:
            status = False
            msg = 'Email or Document does not exist'
            code = 415
            return status, msg, code

        user = UsersDocuments.query.filter(UsersDocuments.document == document, UsersDocuments.email == email).first()
        current_session.delete(user)
        current_session.commit()

        status = True
        msg = 'Document Deleted Successfully'
        code = 200
        return status, msg, code

    except Exception as e:
        print e
        status = False
        msg = 'Our Servers Are currently busy, Try again later'
        code = 500
        return status, msg, code


def patch_assign_doc(http_request):
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
        email = json_payload.get('email')

        doc_exist = UsersDocuments.query.filter_by(document=document).first()
        user_exist= Users.query.filter_by(email=email).first()
        if not doc_exist or not user_exist:
            status = False
            msg = 'User or Document does not exist'
            code = 415
            return status, msg, code

        doc_exist.email = email
        current_session.commit()

        status = True
        msg = 'Document Patched Successfully'
        code = 200
        return status, msg, code


    except Exception as e:
        print e
        status = False
        msg = 'Our Servers Are currently busy, Try again later '
        code = 500
        return status, msg, code

def view_doc_status(http_request, document):
    token = http_request.headers.get('X-Client-ID')
    des_token = verify_auth_token(token)

    email = des_token['token'].get('email')

    try:
        user = Users.query.filter_by(email=email).first()
        if not user:
            status = False
            msg = 'Forbidden!!! You do not have the right for this'
            code = 415
            data = ''
            return status, msg, data, code

        document_status = []

        assign_docs = UsersDocuments.query.filter_by(document=document)

        for docs in assign_docs:
            doc_dict = {}
            document = DocumentMetaData.query.filter_by(document_identifier=docs.document).first()
            doc_dict['Document Path'] = os.path.join(app.config['UPLOAD_FOLDER'], document.document_identifier)
            doc_dict['Name'] = document.name
            doc_dict['Create Date'] = document.Date
            doc_dict['Assigned To'] = docs.email
            document_status.append(doc_dict)

        status = True
        msg = 'Success'
        code = 200
        data = document_status
        return status, msg, data, code

    except Exception as e:
        print e
        status = 'error'
        msg = 'error in connection'
        code = 500
        data = ''
        return msg, status, data, code
