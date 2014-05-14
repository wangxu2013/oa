# coding:utf-8
__author__ = 'johhny'

from scapp import db
from scapp.models import OA_User
from flask.ext.login import current_user

#项目
class OA_Project(db.Model):
    '''
    项目
    '''
    __tablename__='oa_project'
    id = db.Column(db.Integer,primary_key=True)
    project_num=db.Column(db.String(16))#项目编号
    project_name=db.Column(db.String(128))#项目名称
    contract_num=db.Column(db.String(16))#合同编号
    customer=db.Column(db.String(32))#客户名称 将来有客户表填入
    project_describe=db.Column(db.String(128))#项目描述
    org_id=db.Column(db.Integer, db.ForeignKey('oa_org.id')) #所属公司
    manager_id=db.Column(db.Integer, db.ForeignKey('oa_user.id')) #项目经理
    section_id=db.Column(db.Integer, db.ForeignKey('oa_section.id')) #所属部门

    #外键
    org_prj = db.relationship('OA_Org', backref='org_prj')
    manager_fk = db.relationship('OA_User', backref='manager_fk')
    section_fk = db.relationship('OA_Section', backref='section_fk')

    def __init__(self,project_num,project_name,contract_num,customer,project_describe,org_id,manager_id,section_id):
        self.project_name=project_name
        self.project_num=project_num
        self.contract_num=contract_num
        self.customer=customer
        self.project_describe=project_describe
        self.org_id=org_id
        self.manager_id=manager_id
        self.section_id=section_id

    def add(self):
        db.session.add(self)