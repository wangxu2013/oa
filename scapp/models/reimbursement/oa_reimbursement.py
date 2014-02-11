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
    project_id = db.Column(db.Integer, db.ForeignKey('oa_project.id'))#项目编号
    org_id = db.Column(db.Integer, db.ForeignKey('oa_org.id'))#项目编号
    amount = db.Column(db.String(16))#金额
    describe = db.Column(db.String(512))#费用描述
    reason = db.Column(db.Integer)#费用事由
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    is_refuse = db.Column(db.String(1))#拒绝标志
    is_retreat = db.Column(db.String(1))#退回标志
    fail_reason = db.Column(db.String(512))#拒绝或退回原因
    is_paid = db.Column(db.String(1))#付款标志
    init_level = db.Column(db.String(1))#初始状态级别
    status = db.Column(db.String(1))#当前状态

    create_user = db.Column(db.Integer, db.ForeignKey('oa_user.id'))
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)
    paid_date = db.Column(db.DateTime)

    #外键
    project = db.relationship('OA_Project', backref='project')
    #外键
    org_r = db.relationship('OA_Org', backref='project')
    #外键
    create = db.relationship('OA_User', backref='create')
	
    def __init__(self,project_id,org_id,amount,describe,reason,start_date,end_date,
        is_refuse,is_retreat,fail_reason,
        is_paid,init_level,status,paid_date):
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
        self.init_level=init_level
        self.status=status
        self.create_user=current_user.id
        self.create_date=datetime.datetime.now()
        self.modify_user=current_user.id
        self.modify_date=datetime.datetime.now()
        self.paid_date=paid_date

    def add(self):
        db.session.add(self)