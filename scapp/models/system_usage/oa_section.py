# coding:utf-8
from scapp import db

#部门
class OA_Section(db.Model):
    '''
    部门
    '''
    __tablename__='oa_section'
    id = db.Column(db.Integer,primary_key=True)
    section_name=db.Column(db.String(64))#名称
    manager_id=db.Column(db.Integer, db.ForeignKey('oa_user.id')) #项目主管

    #外键
    oa_section_manager = db.relationship('OA_User', backref='oa_section_manager')
    
    def __init__(self,section_name,manager_id):
        self.section_name=section_name
        self.manager_id=manager_id

    def add(self):
        db.session.add(self)