#coding:utf-8
from scapp import db
import datetime

# 项目成员表
class OA_Task_Board(db.Model):
    __tablename__ = 'oa_task_board' 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('oa_user.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('oa_task_main.id'))
    task_content = db.Column(db.String(500))
    create_time = db.Column(db.DateTime)
    finish_time = db.Column(db.DateTime)
    static = db.Column(db.String())
    oa_task_board_ibfk_1 = db.relationship('OA_Task_Main', backref='oa_task_board_ibfk_1')
    oa_task_board_ibfk_2 = db.relationship('OA_User', backref='oa_task_board_ibfk_2')

    def __init__(self, user_id,task_id,task_content,finish_time,static):
        self.user_id = user_id
        self.task_id = task_id
        self.task_content = task_content
        self.create_time = datetime.datetime.now()
        self.finish_time = finish_time
        self.static = static

    def add(self):
        db.session.add(self)