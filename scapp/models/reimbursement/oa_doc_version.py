#coding:utf-8
from scapp import db

# 角色表
class OA_Doc_Version(db.Model):
    __tablename__ = 'oa_doc_version' 
    id = db.Column(db.Integer, primary_key=True)
    doc_id = db.Column(db.Integer, db.ForeignKey('oa_doc.id'))
    version = db.Column(db.Integer)
    attachment = db.Column(db.String)#路径

    oa_doc_version_ibfk_1 = db.relationship('OA_Doc', backref='oa_doc_version_ibfk_1')
    
    def __init__(self, doc_id,version,attachment):
        self.doc_id = doc_id
        self.version = version
        self.attachment = attachment

    def add(self):
        db.session.add(self)