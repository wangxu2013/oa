#coding:utf-8
from scapp import db
import datetime

# 角色表
class OA_Role(db.Model):
    __tablename__ = 'oa_role' 
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(16))
    role_level = db.Column(db.Integer)

    def __init__(self, role_name,role_level):
        self.role_name = role_name
        self.role_level = role_level

    def add(self):
        db.session.add(self)