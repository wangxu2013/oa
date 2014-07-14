#coding:utf-8
from scapp import db
import datetime

from flask.ext.login import current_user

# 角色表
class OA_View_Doc_Privilege(db.Model):
    __tablename__ = 'view_doc_privilege' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    attachment = db.Column(db.String)#路径
    project_id = db.Column(db.Integer)#初始所属项目编号
    org_id = db.Column(db.Integer)#初始所属部门编号
    privilege_operation = db.Column(db.String)
    privilege_master_id = db.Column(db.Integer)
    
    def __init__(self, name,attachment,project_id,org_id,privilege_operation,privilege_master_id):
        self.name = name
        self.attachment = attachment
        self.project_id = project_id
        self.org_id = org_id
        self.privilege_operation = privilege_operation
        self.privilege_master_id = privilege_master_id

    def add(self):
        db.session.add(self)