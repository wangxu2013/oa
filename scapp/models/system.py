#coding:utf-8
from scapp import db
import json
import datetime

from flask.ext.login import current_user

# 用户、角色 关联表
class OA_UserRole(db.Model):
    __tablename__ = 'oa_userrole' 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('oa_user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('oa_role.id'))

    #外键
    role = db.relationship('OA_Role', backref='role')
    #外键
    user = db.relationship('OA_User', backref='user')

    def __init__(self,user_id,role_id):
        self.user_id = user_id
        self.role_id = role_id

    def add(self):
        db.session.add(self)

# 用户表
class OA_User(db.Model):
    __tablename__ = 'oa_user' 
    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(16))
    login_password = db.Column(db.String(32))
    real_name = db.Column(db.String(32))
    sex = db.Column(db.String(1))
    mobile = db.Column(db.String(16))
    department = db.Column(db.Integer, db.ForeignKey('oa_org.id'))
    active = db.Column(db.String(1))
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)

    #外键
    org = db.relationship('OA_Org', backref='org')

    def __init__(self,login_name,login_password,real_name,sex,mobile,department,active):
        self.login_name = login_name
        self.login_password = login_password
        self.real_name = real_name
        self.sex = sex
        self.mobile = mobile
        self.department = department
        self.active = active
        self.create_user = current_user.id
        self.create_date = datetime.datetime.now()
        self.modify_user = current_user.id
        self.modify_date = datetime.datetime.now()

    def add(self):
        db.session.add(self)

    # flask-login 需要的4个函数---start
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
    # flask-login 需要的4个函数---end

# 角色表
class OA_Role(db.Model):
    __tablename__ = 'oa_role' 
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(16))
    role_level = db.Column(db.Integer)

    def __init__(self, role_name, role_level):
        self.role_name = role_name
        self.role_level = role_level

    def add(self):
        db.session.add(self)

# 机构表
class OA_Org(db.Model):
    __tablename__ = 'oa_org' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    pId = db.Column(db.Integer)
    open = db.Column(db.Boolean)
    org_level = db.Column(db.Integer)

    def __init__(self, name, pId,org_level):
        self.name = name
        self.pId = pId
        self.open = True
    	self.org_level = org_level

    def add(self):
        db.session.add(self)