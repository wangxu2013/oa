# coding:utf-8
from scapp import db
from scapp.config import PER_PAGE
from scapp.config import logger
from scapp.config import Approval_type_ORG,Approval_type_PRJ,Approval_type_CAIWU
import scapp.helpers as helpers
import datetime

from flask import Module, session, request, render_template, redirect, url_for, flash
from flask.ext.login import current_user

from scapp.models import OA_Project,OA_Reason,OA_Org,OA_UserRole,OA_Reimbursement

from scapp import app

# 新增费用
@app.route('/xzfy/new_xzfy', methods=['GET','POST'])
def new_xzfy():
    if request.method=='POST':
        try:
            role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
            level = role.role_level #取得用户权限等级
            #提单，自动级别高的部门下
            approval =""
            approval_type=""
            print level
            if str(level)=='5':
                approval_type=Approval_type_CAIWU
            elif str(level)=='6':
                approval=request.form['project_id']
                approval_type=Approval_type_PRJ
            else:
                string = getLastId(request.form['project_id'],Approval_type_PRJ,level)
                if string:
                    app = string.split('.')
                    approval=app[0]
                    approval_type=app[1]
            print "========"
            print approval
            print approval_type
            OA_Reimbursement(approval,approval_type,request.form['project_id'],request.form['org_id'],
                             request.form['amount'],request.form['describe'],request.form['reason'],
                             request.form['start_date'],request.form['end_date'],
                             '0','0','','0',None).add()
                         
            db.session.commit()
            # 消息闪现
            flash('保存成功','success')
        except:
            # 回滚
            db.session.rollback()
            logger.exception('exception')
            # 消息闪现
            flash('保存失败','error')

        return redirect('xzfy/new_xzfy')

    else:
        reasons = OA_Reason.query.order_by("id").all()

        return render_template("bxsq/xzfy/new_xzfy.html",reasons=reasons)
    
# 修改费用
@app.route('/xzfy/edit_xzfy/<int:id>', methods=['GET','POST'])
def edit_xzfy(id):
    if request.method=='POST':
        try:
            reimbursement = OA_Reimbursement.query.filter_by(id=id).first()
            #如果是负责人提单，自动到上级部门或项目
            approval =""
            approval_type=""
            string = getLastId(request.form['project_id'],Approval_type_PRJ,level)
            if string:
                app = string.split('.')
                approval=app[0]
                approval_type=app[1]
            reimbursement.approval = approval
            reimbursement.approval_type = approval_type
            reimbursement.project_id = request.form['project_id']
            reimbursement.org_id = request.form['org_id']
            reimbursement.amount = request.form['amount']
            reimbursement.describe = request.form['describe']
            reimbursement.reason = request.form['reason']
            reimbursement.start_date = request.form['start_date']
            reimbursement.end_date = request.form['end_date']
            
            db.session.commit()
            # 消息闪现
            flash('保存成功','success')
        except:
            # 回滚
            db.session.rollback()
            logger.exception('exception')
            # 消息闪现
            flash('保存失败','error')

        return redirect('grcx/grcx_search')
    else:
        reimbursement = OA_Reimbursement.query.filter_by(id=id).first()
        reasons = OA_Reason.query.order_by("id").all()
        belong_name = OA_Project.query.filter_by(id=reimbursement.project_id).first().project_name
        return render_template("bxsq/xzfy/edit_xzfy.html",reimbursement=reimbursement,reasons=reasons,belong_name=belong_name)

#递归查询级别
def getLastId(id,approval_type,level):
    #项目
    if int(approval_type)==int(Approval_type_PRJ):
        project = OA_Project.query.filter_by(id=id).first()
        if project:
            #如果存在上级项目
            if project.p_project_id:
                #获取上级项目manager级别
                last_project = OA_Project.query.filter_by(id=project.p_project_id).first()
                role = OA_UserRole.query.filter_by(user_id=last_project.manager_id).first().oa_userrole_ibfk_2
                last_level = role.role_level #取得用户权限等级
                if int(last_level)>int(level):
                    return project.id+"."+Approval_type_PRJ
                else:
                    return getLastId(project.p_project_id,Approval_type_PRJ,level)
                    
            #如果存在上级部门
            else:
                #获取上级部门manager级别
                last_org = OA_Org.query.filter_by(id=project.p_org_id).first()
                role = OA_UserRole.query.filter_by(user_id=last_org.manager).first().oa_userrole_ibfk_2
                last_level = role.role_level #取得用户权限等级
                if int(last_level)>int(level):
                    return str(project.p_org_id)+"."+str(Approval_type_ORG)
                else:
                    return getLastId(project.p_org_id,Approval_type_ORG,level)
                    
    #部门
    else:
        org = OA_Org.query.filter_by(id=id).first()
        if org:
            #如果存在上级部门
            if org.pId:
                #获取上级部门manager级别
                last_org = OA_Org.query.filter_by(id=org.pId).first()
                role = OA_UserRole.query.filter_by(user_id=last_org.manager).first().oa_userrole_ibfk_2
                last_level = role.role_level #取得用户权限等级
                if int(last_level)>int(level):
                    return str(org.pId)+"."+str(Approval_type_ORG)
                else:
                    return getLastId(last_org.id,Approval_type_ORG,level)
                    
