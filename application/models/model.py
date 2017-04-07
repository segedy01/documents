"""
Holds the table definitions and other various db transactions
"""

# from werkzeug.security import generate_password_hash, check_password_hash
from passlib.apps import custom_app_context as pwd_context

from application import db
from datetime import  datetime


class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(150))
    roles = db.Column(db.String(10))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __repr__(self):
        return '<User: {}>'.format(self.name)


class DocumentMetaData(db.Model):

    __tablename__ = 'document_meta_data'

    document_identifier = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, index=True)
    Date = db.Column(db.DateTime, default=datetime.now())


class UsersDocuments(db.Model):

    __tablename__ = 'users_document'

    id = db.Column(db.Integer, primary_key=True)
    document = db.Column(db.String(150), db.ForeignKey('document_meta_data.document_identifier'))
    email = db.Column(db.String, db.ForeignKey('users.email'), default=None)

    def __repr__(self):
        return '<User: {}>'.format(self.name)


# class Documents(db.Model):
#     __tablename__ = 'documents'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(150), unique=True)
#
#     def __repr__(self):
#         return '<User: {}>'.format(self.name)