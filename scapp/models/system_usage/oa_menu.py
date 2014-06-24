#coding:utf-8
from scapp import db
import datetime

# 角色表
class OA_Menu(db.Model):
    __tablename__ = 'oa_menu' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    menu_code = db.Column(db.String(16))
    open = db.Column(db.Boolean)
    pId = db.Column(db.Integer)
    level = db.Column(db.Integer)

    def __init__(self, name,menu_code,pId,level):
        self.name = name
        self.menu_code = menu_code
        self.pId = pId
        self.open = True
        self.level = level

    def add(self):
        db.session.add(self)