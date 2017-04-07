import json
from application.models.model import Users
import os
from application import db, app
from werkzeug import secure_filename
from application.utils.utility import is_valid_file


def post_document(http_request, doc_name):

    try:
        file_upload = http_request.files['file']
        # payload = http_request.json
        doc_name = str(doc_name)

        if file_upload:
            filename = secure_filename(file_upload.filename)
            valid_file = is_valid_file(filename)
            print valid_file
            if valid_file[0]:
                new_doc_name = doc_name + '.' + valid_file[1]
                file_upload.save(os.path.join(app.config['UPLOAD_FOLDER'], new_doc_name))
                # print payload.get('email')
                status = True
                msg = 'Documents Gotten'
                code = 200
                return status, msg, code
            status = False
            msg = 'Documents Gone'
            code = 500
            return status, msg, code

    except Exception as e:

        print e
        status = False
        msg = 'User already exist. Contact admin for more information'
        code = 400
        return status, msg, code
