# coding:utf-8
from scapp import db
from scapp.config import PER_PAGE,EMAIL_SERVER,EMAIL_SEND
from scapp.config import logger
from scapp.config import Approval_type_ORG,Approval_type_PRJ,Approval_type_CAIWU
import scapp.helpers as helpers
import datetime,time

from flask import Module, session, request, render_template, redirect, url_for, flash
from flask.ext.login import login_user,current_user

from scapp.models import OA_Project,OA_Reason,OA_Org,OA_User,OA_UserRole,OA_Reimbursement,OA_Email_Url

from scapp import app


from flask.ext.mail import Mail
 
from flask.ext.mail import Message
 
from threading import Thread
import uuid
from scapp.tools.export_excel import export_excel
import xlwt,re

ezxf=xlwt.easyxf #样式转换




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

#费用审批总单
@app.route('/fysp/fysp_total',methods=['GET','POST'])
def fysp_total():
    #搜索条件
    org_id="-1"
    project_id="-1"
    #POST时有搜索条件
    if request.method == 'POST':
        if request.form['org_id']:
            org_id = request.form['org_id']
            project_id = request.form['project_id']
    
    sql =" is_refuse=0 and is_paid =0 "
    #财务总监
    if current_user.id is not 15:
        sql+=" and approval_type!=4 "
    orgAll = OA_Org.query.filter_by(manager=current_user.id).all()
    sql+=" and ("
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
                sql +=" approval_type = 3"
            else:
                sql += " (approval="+org_id+" and approval_type = 1)"
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
            sql += " or (approval in "+app+" and approval_type = 2)"
    #前台选择项目
    else:
        sql += " or (approval="+project_id+" and approval_type = 2)"
    sql+=")"
    sql+=" group by create_user"
    if len(orgAll)>0 or len(da)>0:
        data = db.session.execute("select a.create_user,count(*) as count ,(select real_name from oa_user b where b.id=a.create_user) as real_name,sum(a.amount) as amount from oa_reimbursement a where "+sql).fetchall()
    
    else:
        data=""
    return render_template("bxsq/fysp/fysp_total.html",data=data,org_id=org_id,project_id=project_id)


#费用审批查询详情
@app.route('/fysp/fysp_list/<int:page>/<int:userId>',methods=['GET','POST'])
def fysp_list(page,userId):
    #搜索条件
    org_id="-1"
    project_id="-1"
    #POST时有搜索条件
    if request.method == 'POST':
        if request.form['org_id']:
            org_id = request.form['org_id']
            project_id = request.form['project_id']
    
    sql =" is_refuse=0 and is_paid =0 and create_user="+str(userId)
    # if current_user.id is not 15:
    sql+=" and approval_type!=4 "
    orgAll = OA_Org.query.filter_by(manager=current_user.id).all()
    sql+=" and ("
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
            sql += "(approval in "+appreval
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
                sql +=" approval_type = 3"
            else:
                sql += " (approval="+org_id+" and approval_type = 1)"
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
            sql += " or (approval in "+app+" and approval_type = 2)"
    #前台选择项目
    else:
        sql += " or (approval="+project_id+" and approval_type = 2)"
    if current_user.id==15:
        sql +=" or (approval_type=4 and is_paid=0)"
    sql+=")"
    if len(orgAll)>0 or len(da)>0:
        try:
            data = OA_Reimbursement.query.filter(sql).paginate(page, per_page = PER_PAGE) 
        except:
            data = OA_Reimbursement.query.filter(sql).paginate(page-1, per_page = PER_PAGE) 
    else:
        data=""
    return render_template("bxsq/fysp/fysp_list.html",data=data,org_id=org_id,project_id=project_id,userId=userId)

#费用审批
@app.route('/fysp/fysp_check/<id>/<page>/<create_user>',methods=['GET','POST'])
def fysp_check(id,page,create_user):
    if request.method=='POST':
        result = request.form['decision']
        fail_reason=""
        if str(result) is not '1':
            fail_reason = request.form['fail_reason']
        #审批流程
        approve(current_user.id,id,result,fail_reason) 
        return ""

    else:
        project = OA_Project.query.order_by("id").all()
        reimbursement = OA_Reimbursement.query.filter_by(id=id).first()
        return render_template("bxsq/fysp/check_bxsq.html",reimbursement=reimbursement,project=project,userId=current_user.id,create_user=create_user,parentPage=int(page))
    

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
            #财务总监审批(暂时不用)
            # if reimbursement.approval_type==4:
            #     reimbursement.is_paid = '1'
            #     reimbursement.paid_date= datetime.datetime.now()
            #如果当前是财务审批
            if reimbursement.approval_type==3:
                reimbursement.approval_type=4
            #部门审批阶段
            elif reimbursement.approval_type==1:
                if power=='true':
                    #审批通过进入财务审批
                    reimbursement.approval_type=3
                else:
                    org = OA_Org.query.filter_by(id=reimbursement.approval).first()
                    if org:
                        if org.pId: 
                            #审批通过进入上级部门审批
                            highOrg = OA_Org.query.filter_by(id=org.pId).first()
                            if highOrg.pId:
                                if highOrg.manager==org.manager:
                                    reimbursement.approval=highOrg.pId
                                else:
                                    reimbursement.approval=org.pId                            
                                reimbursement.approval_type = 1
                            else:
                               reimbursement.approval=org.pId 
                               reimbursement.approval_type = 1
                        else:
                            #审批通过进入财务审批
                            reimbursement.approval_type=3
            #项目审批阶段
            else:
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
            if reimbursement.approval_type is not 4:
                #邮件通知
                SendMail(reimbursement)
        #拒绝
        if result=='2':
            reimbursement.is_refuse = '1'
            reimbursement.fail_reason = reason
        #退回
        if result=='3':
            reimbursement.is_retreat = '1'
            reimbursement.approval=reimbursement.project_id
            reimbursement.approval_type= '2'
            reimbursement.fail_reason = reason
        email_url = OA_Email_Url.query.filter_by(manager=current_user.id,list_id=reimbursement.id).first()
        if email_url:
            email_url.list_type=result
        db.session.commit()
        # 消息闪现
        flash('保存成功','success')
    except:
        # 回滚
        db.session.rollback()
        logger.exception('exception')
        # 消息闪现
        flash('保存失败','error')

#费用支付搜索
@app.route('/fysp/fyzf_search',methods=['GET'])
def fyzf_search():
    
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
    level = role.role_level #取得用户权限等级
    date = time.strftime('%Y-%m-%d',time.localtime(time.time()-2*30*24*60*60))
    user = OA_User.query.all()
    
    orgs = OA_Org.query.all()
            
    projects = OA_Project.query.all()
            
    return render_template("bxsq/fysp/fyzf_search.html",level=level,beg_date=date,user=user,orgs=orgs,projects=projects)

#费用支付总单
@app.route('/fysp/fyzf_total',methods=['GET','POST'])
def fyzf_total():
    #搜索条件
    org_id="-1"
    project_id="-1"
    #POST时有搜索条件
    if request.method == 'POST':
        if request.form['org_id']:
            org_id = request.form['org_id']
            project_id = request.form['project_id']
    
    sql =" is_refuse=0 and is_paid =0 and approval_type=4 "

    if float(org_id) > -1:
        if float(project_id) != -1:
            sql+=" and (org_id="+org_id+" and project_id="+project_id+")"
        else:
            sql+=" and org_id="+org_id
    else:
        if float(project_id) >-1:
            sql+="and project_id="+project_id
    sql+=" group by create_user"
    if current_user.id==2:
        data = db.session.execute("select a.create_user,count(*) as count ,(select real_name from oa_user b where b.id=a.create_user) as real_name,sum(a.amount) as amount from oa_reimbursement a where "+sql).fetchall()
    else:
        data=""
    return render_template("bxsq/fysp/fyzf_total.html",data=data,org_id=org_id,project_id=project_id)

#费用支付查询详情
@app.route('/fysp/fyzf_list/<int:page>/<int:userId>',methods=['GET','POST'])
def fyzf_list(page,userId):
    #搜索条件
    org_id="-1"
    project_id="-1"
    #POST时有搜索条件
    if request.method == 'POST':
        if request.form['org_id']:
            org_id = request.form['org_id']
            project_id = request.form['project_id']
    
    sql =" is_refuse=0 and is_paid =0 and approval_type=4 and create_user="+str(userId)

    if float(org_id) > -1:
        if float(project_id) != -1:
            sql+=" and (org_id="+org_id+" and project_id="+project_id+")"
        else:
            sql+=" and org_id="+org_id
    else:
        if float(project_id) != -1:
            sql+=" and project_id="+project_id
    try:
        data = OA_Reimbursement.query.filter(sql).paginate(page, per_page = PER_PAGE) 
    except:
        data = OA_Reimbursement.query.filter(sql).paginate(page-1, per_page = PER_PAGE) 
    return render_template("bxsq/fysp/fyzf_list.html",data=data,org_id=org_id,project_id=project_id,userId=userId)

#费用支付
@app.route('/fysp/fyzf_check/<id>/<page>/<create_user>',methods=['GET','POST'])
def fyzf_check(id,page,create_user):
    if request.method=='POST':
        try:
            #报销单信息
            reimbursement = OA_Reimbursement.query.filter_by(id=id).first()  
            reimbursement.is_paid=1
            reimbursement.paid_date= datetime.datetime.now()
            db.session.commit()
            # 消息闪现
            flash('保存成功','success')
        except:
            # 回滚
            db.session.rollback()
            logger.exception('exception')
            # 消息闪现
            flash('保存失败','error')
    else:
        project = OA_Project.query.order_by("id").all()
        reimbursement = OA_Reimbursement.query.filter_by(id=id).first()
        return render_template("bxsq/fysp/checkzf_bxsq.html",reimbursement=reimbursement,project=project,userId=current_user.id,create_user=create_user,parentPage=int(page))

#费用批量支付
@app.route('/fysp/fyzf_pay/<id>/<int:page>/<userId>',methods=['GET','POST'])
def fyzf_pay(id,page,userId):
    if request.method=='POST':  
        try:
            if "." in id:
                value=id.split(".")
                for obj in value:
                    reimbursement = OA_Reimbursement.query.filter_by(id=obj).first()  
                    reimbursement.is_paid=1
                    reimbursement.paid_date= datetime.datetime.now() 
            else:
                value=id
                reimbursement = OA_Reimbursement.query.filter_by(id=value).first()  
                reimbursement.is_paid=1
                reimbursement.paid_date= datetime.datetime.now() 
            db.session.commit()
            # 消息闪现
            flash('支付成功','success')
        except:
            # 回滚
            db.session.rollback()
            logger.exception('exception')
            # 消息闪现
            flash('支付失败','error')
    #搜索条件
        org_id="-1"
        project_id="-1"
        #POST时有搜索条件
        if request.method == 'POST':
            if request.form['org_id']:
                org_id = request.form['org_id']
                project_id = request.form['project_id']
        
        sql =" is_refuse=0 and is_paid =0 and approval_type=4 and create_user="+str(userId)

        if float(org_id) > -1:
            if float(project_id) != -1:
                sql+=" and (org_id="+org_id+" and project_id="+project_id+")"
            else:
                sql+=" and org_id="+org_id
        else:
            if float(project_id) != -1:
                sql+=" and project_id="+project_id
        try:
            data = OA_Reimbursement.query.filter(sql).paginate(page, per_page = PER_PAGE) 
        except:
            data = OA_Reimbursement.query.filter(sql).paginate(page-1, per_page = PER_PAGE) 
        return render_template("bxsq/fysp/fyzf_list.html",data=data,org_id=org_id,project_id=project_id,userId=userId)

#费用支付Excel下载
@app.route('/fysp/fyzf_Excel',methods=['GET','POST'])
def fyzf_Excel():
    beg_date = request.form['beg_date'] + " 00:00:00"
    end_date = request.form['end_date'] + " 23:59:59"
    is_paid = request.form['is_paid']

    sql = "SELECT b.name,c.real_name,d.project_name,a.amount,a.`describe`,a.create_date,(case is_paid when '0' then '未支付' \
        when '1' then '已支付' end) as paid,a.paid_date FROM oa_reimbursement a, oa_org b, oa_user c,oa_project d WHERE\
        a.org_id = b.id AND a.create_user = c.id and a.project_id=d.id"
    sql += " and a.create_date between '" + beg_date + "' and '" + end_date + "'"
    if float(is_paid) !=-1:
        sql+=" and a.is_paid="+str(is_paid)
    sql +="order by a.is_paid,c.real_name,b.name"
    data=db.session.execute(sql).fetchall()


    exl_hdngs=['费用所属单位','申请人','项目','金额','报销事由','创建时间','审批状态','支付时间']
    types=     'text   text   text      text      text     datetime    text   datetime'.split()
    exl_hdngs_xf=ezxf('font: bold on;align: wrap on,vert centre,horiz center')
    types_to_xf_map={
        'int':ezxf(num_format_str='#,##0'),
        'date':ezxf(num_format_str='yyyy-mm-dd'),
        'datetime':ezxf(num_format_str='yyyy-mm-dd HH:MM:SS'),
        'ratio':ezxf(num_format_str='#,##0.00%'),
        'text':ezxf(),
        'price':ezxf(num_format_str='￥#,##0.00')
    }

    data_xfs=[types_to_xf_map[t] for t in types]
    date=datetime.datetime.now()
    year=date.year
    month=date.month
    day=date.day
    filename=str(year)+'_'+str(month)+'_'+str(day)+'_'+'报销费用支付详情'+'.xls'
    exp=export_excel()
    return exp.export_download(filename,'报销费用支付详情表',exl_hdngs,data,exl_hdngs_xf,data_xfs)

#邮件发送
def SendMail(reimbursement):
        #获取邮件地址
        manager_id = ""
        if str(reimbursement.approval_type)=='1':
           org = OA_Org.query.filter_by(id=reimbursement.approval).first()
           manager_id = org.manager
        elif str(reimbursement.approval_type)=='2':
           pro = OA_Project.query.filter_by(id=reimbursement.approval).first()
           manager_id = pro.manager_id
        else:
            org = OA_Org.query.filter_by(is_caiwu='1').first()
            manager_id = org.manager
        user = OA_User.query.filter_by(id=manager_id).first()
        email = user.email
        if not email:
            return ""
        #创建uuid
        uu = uuid.uuid1()
        url = EMAIL_SERVER+"/fysp/email_return/"+str(uu)
        msg = Message('OA报销审批提醒',sender=EMAIL_SEND,recipients=[email])
        msg.body = "text body"
        msg.html = "<div style='border:1px solid #94c1dc;margin-bottom:10px;width:800px;'><table style='border-collapse:collapse;width:800px;'>\
                    <thead><tr style='background:#afd5eb;'><th style='border:1px solid #FFF;padding:10px;'>费用所属单位</th>\
                    <th style='border:1px solid #FFF;'>项目</th>\
                    <th style='border:1px solid #FFF;'>申请人</th>\
                    <th style='border:1px solid #FFF;'>金额</th>\
                    <th style='border:1px solid #FFF;'>报销事由</th></tr></thead>\
                    <tbody><tr style='text-align:center;background:#efefef;'>\
                    <td style='border:1px solid #FFF;color:#333333;padding:5px;'>"+reimbursement.oa_reimbursement_ibfk_3.name+"</td>\
                    <td style='border:1px solid #FFF;color:#333333;'>"+reimbursement.oa_reimbursement_ibfk_3.name+"</td>\
                    <td style='border:1px solid #FFF;color:#333333;'>"+reimbursement.oa_reimbursement_ibfk_2.real_name+"</td>\
                    <td style='border:1px solid #FFF;color:red;font-weight:bold;'>"+reimbursement.amount+"</td>\
                    <td style='border:1px solid #FFF;color:#333333;'>"+reimbursement.oa_reimbursement_ibfk_5.reason_name+"</td></tr></tbody></table></div>\
                    <div><a href='"+url+"' style='color:#0088cc;text-decoration:none;'>点击查看详情</a></div>"
        thr = Thread(target=send_async_email,args=[app,msg,reimbursement.id,manager_id,uu])
        thr.start()
        return "OK"

def send_async_email(app,msg,list_id,manager_id,uu):
        with app.app_context():
                try:  
                    OA_Email_Url(list_id,manager_id,uu,0).add()
                    db.session.commit()
                    mail = Mail(app)
                    mail.send(msg)
                except:
                    # 回滚
                    db.session.rollback()
                    logger.exception('exception') 

#邮件链接
@app.route('/fysp/email_return/<random_uuid>',methods=['GET','POST'])
def email_return(random_uuid):
    email = OA_Email_Url.query.filter_by(random_uuid=random_uuid).first()
    if email:
        #自动登录
        user = OA_User.query.filter_by(id=email.manager).first()
        login_user(user)
        project = OA_Project.query.order_by("id").all()
        reimbursement = OA_Reimbursement.query.filter_by(id=email.list_id).first()
        return render_template("bxsq/fysp/email_bxsq.html",reimbursement=reimbursement,project=project,email=email)
    else:
        return redirect("/login")

#邮件提交
@app.route('/fysp/email_check/<id>',methods=['GET','POST'])
def email_check(id):
    if request.method=='POST':
        try:
            result = request.form['decision']
            fail_reason=""
            if str(result) is not '1':
                fail_reason = request.form['fail_reason']
            
            db.session.commit()
            #审批流程
            approve(current_user.id,id,result,fail_reason)
        except:
            db.session.rollback()
            logger.exception('exception') 
    return redirect("/welcome")

#返回首页
@app.route('/fysp/email_check_return',methods=['GET','POST'])
def email_check_return():
    return redirect("/login")
