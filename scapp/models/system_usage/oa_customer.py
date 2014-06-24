#coding:utf-8
from scapp import db
import datetime

# 角色表
class OA_Customer(db.Model):
    __tablename__ = 'oa_customer' 
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(32))

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add(self):
        db.session.add(self)