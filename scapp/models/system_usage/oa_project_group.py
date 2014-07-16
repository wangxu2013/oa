#coding:utf-8
from scapp import db
import datetime

from flask.ext.login import current_user

# 项目组表j
class OA_ProjectGroup(db.Model):
    __tablename__ = 'oa_project_group' 
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer)
    type = db.Column(db.String(11))
    user_id = db.Column(db.Integer, db.ForeignKey('oa_user.id'))
    
    oa_project_group_ibfk_1 = db.relationship('OA_User', backref='oa_project_group_ibfk_1')
    
    def __init__(self, project_id, type,user_id):
        self.project_id = project_id
        self.type = type
        self.user_id = user_id

    def add(self):
        db.session.add(self)