# coding:utf-8
from scapp import db
from scapp.config import PER_PAGE
from scapp.config import logger
from scapp.config import Approval_type_ORG,Approval_type_PRJ,Approval_type_CAIWU
import scapp.helpers as helpers
import datetime,time

from flask import Module, session, request, render_template, redirect, url_for, flash
from flask.ext.login import current_user

from scapp.models import OA_Project,OA_Reason,OA_Org,OA_User,OA_UserRole,OA_Reimbursement

from scapp import app

#费用审批搜索
@app.route('/fysp/fysp_search',methods=['GET'])
def fysp_search():
    
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
    level = role.role_level #取得用户权限等级
    date = time.strftime('%Y-%m-%d',time.localtime(time.time()-2*30*24*60*60))
    user = OA_User.query.all()
    
    orgs = OA_Org.query.filter_by(manager=current_user.id).all()
            
    projects = OA_Project.query.filter_by(manager_id=current_user.id).all()
            
    return render_template("bxsq/fysp/fysp_search.html",level=level,beg_date=date,user=user,orgs=orgs,projects=projects)

#费用审批搜索
@app.route('/fysp/fysp_list/<int:page>',methods=['GET','POST'])
def fysp_list(page):
    #搜索条件
    beg_date=""
    end_date=""
    org_id="-1"
    project_id="-1"
    #POST时有搜索条件
    if request.method == 'POST':
        if request.form['beg_date']:
            beg_date = request.form['beg_date'] + " 00:00:00"
            end_date = request.form['end_date'] + " 23:59:59"
            org_id = request.form['org_id']
            project_id = request.form['project_id']
    
    sql =" is_refuse=0 and is_paid =0 and ("
    orgAll = OA_Org.query.filter_by(manager=current_user.id).all()
    if org_id == "-1":
        if len(orgAll)>0:
            appreval ="("
            #判断是否含有财务部门
            type ='1'
            for i in orgAll:
                appreval=appreval+str(i.id)+","
                if i.is_caiwu==1:
                    type='2'
            if len(appreval)>1:
                appreval=appreval[0:len(appreval)-1]
            appreval+=")"
            sql += " (approval in "+appreval
            #含财务部门
            if type=='2':
                sql += " or approval_type = 3)"
            else:
                sql += " and approval_type=1)"
        else:
           sql +=" approval is null" 
    else:
        org = OA_Org.query.filter_by(id=org_id).first()
        if org:
            if org.is_caiwu=='1':
                sql +="  approval_type = 3"
            else:
                sql += "  (approval="+org_id+" and approval_type = 1)"
    #前台没有选择项目
    da = OA_Project.query.filter_by(manager_id=current_user.id).all()
    if project_id == "-1":
        if len(da)>0:
            app ="("
            for i in da:
                app=app+str(i.id)+","
            if len(app)>1:
                app=app[0:len(app)-1]
            app+=")"
            sql += " or (approval in "+app+" and approval_type = 2))"
    #前台选择项目
    else:
        sql += " or (approval="+project_id+" and approval_type = 2))"
    #POST时有搜索条件
    if request.method == 'POST':
        if request.form['beg_date']:
            sql += " and create_date between '"+beg_date+"' and '"+end_date+"'"
    if len(orgAll)>0 or len(da)>0:
        data = OA_Reimbursement.query.filter(sql).paginate(page, per_page = PER_PAGE)
    else:
        data=0
    return render_template("bxsq/fysp/fysp_list.html",data=data,beg_date=beg_date,end_date=end_date,
                           org_id=org_id,project_id=project_id)

#费用审批
@app.route('/fysp/fysp_check/<id>/<page>',methods=['GET','POST'])
def fysp_check(id,page):
    if request.method=='POST':
        result = request.form['decision']
        fail_reason=""
        if str(result) is not '1':
            fail_reason = request.form['fail_reason']
        #审批流程
        approve(current_user.id,id,result,fail_reason) 
        return redirect('fysp/fysp_list/'+str(page))

    else:
        role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
        project = OA_Project.query.order_by("id").all()
        reimbursement = OA_Reimbursement.query.filter_by(id=id).first()
        return render_template("bxsq//fysp/check_bxsq.html",reimbursement=reimbursement,project=project,role=role,parentPage=int(page))
    

#审批详细方法
def approve(user_id,expense_id,result,reason):
    try:
        #报销单信息
        reimbursement = OA_Reimbursement.query.filter_by(id=expense_id).first()
        #通过
        if result=='1':
            #金额权限
            power = 'false'
            #查询金额是否在审批权限内
            amount_limit=""
            if reimbursement.approval_type==1:
                org = OA_Org.query.filter_by(id=reimbursement.approval).first()
                amount_limit = org.amount
            elif reimbursement.approval_type==2:
                project = OA_Project.query.filter_by(id=reimbursement.approval).first()
                amount_limit = project.amount
            #财务无需比较
            if int(reimbursement.approval_type) is not 3:
                if float(reimbursement.amount)<=float(amount_limit):
                    power= 'true'
            #如果当前是财务审批
            if reimbursement.approval_type==3:
                #标记已付款
                reimbursement.is_paid = '1'
                reimbursement.paid_date= datetime.datetime.now()
            #项目审批阶段
            elif reimbursement.approval_type==2:
                if power=='true':
                    #审批通过进入财务审批
                    reimbursement.approval_type=3
                else:
                    project = OA_Project.query.filter_by(id=reimbursement.approval).first()
                    if project:
                        if project.p_project_id:
                            #审批通过进入上级项目审批
                            reimbursement.approval=project.p_project_id
                        else:
                            #审批通过进入上级部门审批(判断是否同一领导)
                            org = OA_Org.query.filter_by(id=project.p_org_id).first()
                            if org:
                                if int(org.manager)==int(project.manager_id):
                                   reimbursement.approval=org.pId
                                else:
                                    reimbursement.approval=project.p_org_id
                            reimbursement.approval_type = 1
            #部门审批阶段
            else:
                if power=='true':
                    #审批通过进入财务审批
                    reimbursement.approval_type=3
                else:
                    org = OA_Org.query.filter_by(id=reimbursement.approval).first()
                    if org:
                        if org.pId: 
                            #审批通过进入上级部门审批
                            reimbursement.approval=project.p_project_id
                        else:
                            #审批通过进入财务审批
                            reimbursement.approval_type=3

        #拒绝
        if result=='2':
            reimbursement.is_refuse = '1'

        #退回
        if result=='3':
            reimbursement.is_retreat = '1'
            reimbursement.approval=reimbursement.project_id
            reimbursement.approval_type= '2'
        reimbursement.fail_reason = reason
        db.session.commit()
        # 消息闪现
        flash('保存成功','success')
    except:
        # 回滚
        db.session.rollback()
        logger.exception('exception')
        # 消息闪现
        flash('保存失败','error')