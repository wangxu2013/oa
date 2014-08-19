#coding:utf-8
from scapp import db

# 用户表
class OA_Email_Url(db.Model):
    __tablename__ = 'oa_email_url' 
    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer)
    manager = db.Column(db.Integer)
    random_uuid = db.Column(db.String(50))
    


    def __init__(self,list_id,manager,random_uuid):
        self.list_id = list_id
        self.manager = manager
        self.random_uuid = random_uuid

    def add(self):
        db.session.add(self)