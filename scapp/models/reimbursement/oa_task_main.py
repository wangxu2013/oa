#coding:utf-8
from scapp import db
import datetime
from flask.ext.login import current_user

# 项目主表
class OA_Task_Main(db.Model):
    __tablename__ = 'oa_task_main' 
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(64))
    content = db.Column(db.String(200))
    create_user = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    delete = db.Column(db.Integer)

    def __init__(self, subject,content):
        self.subject = subject
        self.content = content
        self.create_user = current_user.id
        self.create_time = datetime.datetime.now()
        self.delete = 0

    def add(self):
        db.session.add(self)