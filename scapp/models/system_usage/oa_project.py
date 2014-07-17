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
    project_describe=db.Column(db.String(128))#项目描述
    p_org_id=db.Column(db.Integer, db.ForeignKey('oa_org.id')) #所属公司
    p_project_id=db.Column(db.Integer) #所属项目
    customer_id=db.Column(db.Integer, db.ForeignKey('oa_customer.id')) #所属客户
    manager_id = db.Column(db.Integer, db.ForeignKey('oa_user.id')) #所属公司
    treeType=db.Column(db.Integer) #树中显示
    amount = db.Column(db.String)
    open = db.Column(db.Boolean)
    
    #外键
    oa_project_ibfk_1 = db.relationship('OA_Org', backref='oa_project_ibfk_1')
    oa_project_ibfk_3 = db.relationship('OA_Customer', backref='oa_project_ibfk_3')
    oa_project_ibfk_4 = db.relationship('OA_User', backref='oa_project_ibfk_4')

    def __init__(self,project_num,project_name,contract_num,project_describe,p_org_id,p_project_id,customer_id,treeType):
        self.project_name=project_name
        self.project_num=project_num
        self.contract_num=contract_num
        self.project_describe=project_describe
        self.p_org_id=p_org_id
        self.p_project_id=p_project_id
        self.customer_id=customer_id
        self.open = True
        self.treeType=treeType

    def add(self):
        db.session.add(self)