#coding:utf-8
from scapp import db
import datetime

# 项目成员表
class OA_Task_User(db.Model):
    __tablename__ = 'oa_task_user' 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('oa_user.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('oa_task_main.id'))

    oa_task_user_ibfk_1 = db.relationship('OA_Task_Main', backref='oa_task_user_ibfk_1')
    oa_task_user_ibfk_2 = db.relationship('OA_User', backref='oa_task_user_ibfk_2')

    def __init__(self, user_id,task_id):
        self.user_id = user_id
        self.task_id = task_id

    def add(self):
        db.session.add(self)