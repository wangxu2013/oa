#coding:utf-8
from scapp import db
import datetime

from flask.ext.login import current_user

# 机构表
class OA_Org(db.Model):
    __tablename__ = 'oa_org' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    pId = db.Column(db.Integer)
    open = db.Column(db.Boolean)
    manager = db.Column(db.Integer, db.ForeignKey('oa_user.id'))
    org_level = db.Column(db.Integer)
    amount = db.Column(db.String)
    is_caiwu = db.Column(db.Integer)
    
    #外键
    oa_org_ibfk_2 = db.relationship('OA_User', backref='oa_org_ibfk_2')
    
    def __init__(self, name, pId,org_level):
        self.name = name
        self.pId = pId
        self.open = True
        self.org_level = org_level

    def add(self):
        db.session.add(self)