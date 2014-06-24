#coding:utf-8
from scapp import db
import datetime

# 角色表
class OA_Reason(db.Model):
    __tablename__ = 'oa_reason' 
    id = db.Column(db.Integer, primary_key=True)
    reason_name = db.Column(db.String(64))

    def __init__(self, reason_name):
        self.reason_name = reason_name

    def add(self):
        db.session.add(self)