# coding:utf-8
__author__ = 'johhny'
import datetime
from flask.ext.login import current_user
from scapp import db
# 费用报销
class OA_Reimbursement(db.Model):
    '''
    费用报销
    '''
    __tablename__ = 'oa_reimbursement' 
    id = db.Column(db.Integer, primary_key=True)
    approval = db.Column(db.Integer)
    approval_type = db.Column(db.Integer)#1-部门，2-项目，3-财务部门
    project_id = db.Column(db.Integer, db.ForeignKey('oa_project.id'))#初始所属项目编号
    org_id = db.Column(db.Integer, db.ForeignKey('oa_org.id'))#初始所属公司编号
    amount = db.Column(db.String(16))#金额
    describe = db.Column(db.String(512))#费用描述
    reason = db.Column(db.Integer, db.ForeignKey('oa_reason.id'))#费用事由
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    is_refuse = db.Column(db.String(1))#拒绝标志
    is_retreat = db.Column(db.String(1))#退回标志
    fail_reason = db.Column(db.String(512))#拒绝或退回原因
    is_paid = db.Column(db.String(1))#付款标志
    paid_date = db.Column(db.DateTime)
    
    create_user = db.Column(db.Integer, db.ForeignKey('oa_user.id'))
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)
    
    #外键
    oa_reimbursement_ibfk_1 = db.relationship('OA_Project', backref='oa_reimbursement_ibfk_1')
    oa_reimbursement_ibfk_2 = db.relationship('OA_User',foreign_keys=[create_user], backref='oa_reimbursement_ibfk_2')
    oa_reimbursement_ibfk_3 = db.relationship('OA_Org', backref='oa_reimbursement_ibfk_3')
    oa_reimbursement_ibfk_5 = db.relationship('OA_Reason', backref='oa_reimbursement_ibfk_5')
    
    def __init__(self,approval,approval_type,project_id,org_id,amount,describe,reason,start_date,end_date,
        is_refuse,is_retreat,fail_reason,is_paid,paid_date):
        self.approval=approval
        self.approval_type = approval_type
        self.project_id=project_id
        self.org_id=org_id
        self.amount=amount
        self.describe=describe
        self.reason=reason
        self.start_date=start_date
        self.end_date=end_date
        self.is_refuse=is_refuse
        self.is_retreat=is_retreat
        self.fail_reason=fail_reason
        self.is_paid=is_paid
        self.paid_date=paid_date
        self.create_user=current_user.id
        self.create_date=datetime.datetime.now()
        self.modify_user=current_user.id
        self.modify_date=datetime.datetime.now()
    
    def add(self):
        db.session.add(self)