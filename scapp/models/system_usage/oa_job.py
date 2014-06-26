#coding:utf-8
from scapp import db
import datetime

# 角色表
class OA_Job(db.Model):
    __tablename__ = 'oa_job' 
    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(64))

    def __init__(self, job_name):
        self.job_name = job_name

    def add(self):
        db.session.add(self)