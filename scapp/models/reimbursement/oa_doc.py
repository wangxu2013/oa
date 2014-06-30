#coding:utf-8
from scapp import db
import datetime

from flask.ext.login import current_user

# 角色表
class OA_Doc(db.Model):
    __tablename__ = 'oa_doc' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    project_id = db.Column(db.Integer, db.ForeignKey('oa_project.id'))#初始所属项目编号
    org_id = db.Column(db.Integer, db.ForeignKey('oa_org.id'))#初始所属项目编号
    attachment = db.Column(db.String)#路径
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)

    oa_doc_ibfk_1 = db.relationship('OA_Project', backref='oa_doc_ibfk_1')
    oa_doc_ibfk_2 = db.relationship('OA_Org', backref='oa_doc_ibfk_2')
    
    def __init__(self, name,project_id,org_id,attachment):
        self.name = name
        self.project_id = project_id
        self.org_id = org_id
        self.attachment = attachment
        self.create_user = current_user.id
        self.create_date = datetime.datetime.now()
        self.modify_user = current_user.id
        self.modify_date = datetime.datetime.now()

    def add(self):
        db.session.add(self)