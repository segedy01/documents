import random
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from application.models.model import DocumentMetaData


valid_extension = ['jpeg', 'pdf', 'jpg', 'docx', 'doc', 'png', 'txt', 'text']


def generate_auth_token(value):
    s = Serializer(secret_key='SECRET_KEY')
    return s.dumps({'token': value})


def verify_auth_token(token):
    s = Serializer(secret_key='SECRET_KEY')
    try:
        data = s.loads(token)
        return data

    except Exception as e:
        return e

def is_valid_file(filename):
    split_file = filename.split('.')
    extension = split_file[-1]
    if extension in valid_extension:
        return True, extension
    return False, None


def code_gen(name, size=10, main_phone=None):
    """
        a simple function to generate random number.
        it is called a lot during the course of this work.

        Args:
            name(str): collects the buyers name
            (context of where its been called. also plain strings can be passed
            in i.e all the lowercase or a mixture as the case may warrant)in the bid
            to make the number generation random enough.

        Kwargs:
            size(int):the length of the string to be generated
            phone_numbers(int): (optional) phone number to make the generation more random.
                plain integer values can also be passed in still

        Returns: a random string(str)
    """

    if main_phone:
        available_char = name + str(main_phone)
    else:
        available_char = name
    return ''.join(random.choice(available_char) for _ in range(size))


def check_if_doc_exist(doc_name, name):
    """
        A recursive function to check if an id given to it exists in the
        database. It generates a new random string if it exists and check
        to make sure the newly generated string doesnt exist

        Args:
            record_id(str): the unique id passed to it to query the database with
            name(str): required when generating a new string
            address(str): optional  when generating a new string
            main_phone(int/str): optional when generating a new string
    """
    try:
        record = DocumentMetaData.query.filter_by(document_identifier=doc_name).first()
        if record:
            doc_name = code_gen(name=name)
            record = check_if_doc_exist(doc_name)
            return record
        else:
            return doc_name
    except Exception as e:
        print e
        return " Something we dont understand went wrong"