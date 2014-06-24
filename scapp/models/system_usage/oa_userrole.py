#coding:utf-8
from scapp import db
import datetime

from flask.ext.login import current_user

# 用户、角色 关联表
class OA_UserRole(db.Model):
    __tablename__ = 'oa_userrole' 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('oa_user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('oa_role.id'))

    #外键
    oa_userrole_ibfk_1 = db.relationship('OA_User', backref='oa_userrole_ibfk_1')
    oa_userrole_ibfk_2 = db.relationship('OA_Role', backref='oa_userrole_ibfk_2')

    def __init__(self,user_id,role_id):
        self.user_id = user_id
        self.role_id = role_id

    def add(self):
        db.session.add(self)