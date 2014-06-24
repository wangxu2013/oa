# coding:utf-8

from flask import Module,request, render_template,flash,redirect
from flask.ext.login import login_user, logout_user, current_user, login_required
from scapp.models import OA_Org,OA_Project
from scapp.models import OA_User
from scapp.models import OA_UserRole
from scapp.models import OA_Reimbursement
from scapp.models import OA_Privilege
from scapp.logic.reimbursement import costs_statistics
from scapp.config import logger
from scapp import app
from scapp import db

import hashlib

#get md5 of a input string  
def GetStringMD5(str):  
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest() 
	
# 登陆
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = OA_User.query.filter_by(login_name=request.form['login_name'], login_password=GetStringMD5(request.form['login_password'])).first()
        if user:
            login_user(user)
            role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
            privileges = OA_Privilege.query.filter_by(privilege_master="OA_Role",privilege_master_id=role.id,privilege_access="OA_Menu").all()
            
            count_1=len(OA_Reimbursement.query.filter_by(create_user=current_user.id,is_paid=0).all())
            count_2=getCount()
            
            orgs = OA_Org.query.filter_by(manager=current_user.id).all()
            result = []
            for obj in orgs:
                tmp = {}
                tmp["name"] = obj.name
                tmp["total_apply"]=costs_statistics.get_total_apply_costs(obj.id)
                tmp["total_paid"]=costs_statistics.get_total_paid_costs(obj.id)
                tmp["monthly"]=costs_statistics.get_monthly_paid_costs(obj.id)
                tmp["season"]=costs_statistics.get_season_paid_costs(obj.id)
                result.append(tmp)
                
            return render_template("welcome.html",role=role,count_1=count_1,count_2=count_2,result=result,privileges=privileges)
        else:
            flash('用户名或密码错误','error')
            return render_template("login.html")

    else:
        return render_template("login.html")

# 注销
@app.route('/logout')
def logout():
    logout_user()
    return render_template("login.html")
    
# 欢迎界面
@app.route('/welcome', methods=['GET'])
@login_required
def welcome():
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
    privileges = OA_Privilege.query.filter_by(privilege_master="OA_Role",privilege_master_id=role.id,privilege_access="OA_Menu").all()
    
    count_1=len(OA_Reimbursement.query.filter_by(create_user=current_user.id,is_paid=0).all())
    count_2=getCount()
    
    orgs = OA_Org.query.filter_by(manager=current_user.id).all()
    result = []
    for obj in orgs:
        tmp = {}
        tmp["name"] = obj.name
        tmp["total_apply"]=costs_statistics.get_total_apply_costs(obj.id)
        tmp["total_paid"]=costs_statistics.get_total_paid_costs(obj.id)
        tmp["monthly"]=costs_statistics.get_monthly_paid_costs(obj.id)
        tmp["season"]=costs_statistics.get_season_paid_costs(obj.id)
        result.append(tmp)
                
    return render_template("welcome.html",role=role,count_1=count_1,count_2=count_2,result=result,privileges=privileges)

# 系统管理
@app.route('/xxgl', methods=['GET'])
@login_required
def xxgl():
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
    privileges = OA_Privilege.query.filter_by(privilege_master="OA_Role",privilege_master_id=role.id,privilege_access="OA_Menu").all()
    return render_template("index.html",menu = 'xxgl',role=role,privileges=privileges)

# 系统管理
@app.route('/xtgl', methods=['GET'])
@login_required
def xtgl():
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
    privileges = OA_Privilege.query.filter_by(privilege_master="OA_Role",privilege_master_id=role.id,privilege_access="OA_Menu").all()
    return render_template("index.html",menu = 'xtgl',role=role,privileges=privileges)

# 待审批
@app.route('/dsp', methods=['GET'])
@login_required
def dsp():
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
    privileges = OA_Privilege.query.filter_by(privilege_master="OA_Role",privilege_master_id=role.id,privilege_access="OA_Menu").all()
    return render_template("index.html",menu = 'dsp',role=role,privileges=privileges)

# 修改密码
@app.route('/change_password/<int:id>', methods=['GET','POST'])
def change_password(id):
    if request.method == 'POST':
        try:
            user = OA_User.query.filter_by(id=id).first()
            if user.login_password == GetStringMD5(request.form['old_password']):
                user.login_password = GetStringMD5(request.form['login_password'])
            else:
                raise Exception

            # 事务提交
            db.session.commit()
            # 消息闪现
            flash('修改密码成功，请重新登录！','success')

        except:
            # 回滚
            db.session.rollback()
            logger.exception('exception')
            # 消息闪现
            flash('修改密码失败，为保障安全，请重新登录后再尝试修改！','error')

        logout_user()
        return redirect("login")
    else:
        return render_template("change_password.html")

#首页获取待审核项目数
def getCount():
    count_2=0
    #查询待审批
    sql =" is_paid=0 "
    orgAll = OA_Org.query.filter_by(manager=current_user.id).all()
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
        sql += "and (approval in "+appreval
        #含财务部门
        if type=='2':
            sql += " or approval_type = 3)"
        else:
            sql += " and approval_type=1)"
    else:
       sql +="and approval is null" 
    da = OA_Project.query.filter_by(manager_id=current_user.id).all()
    if len(da)>0:
        app ="("
        for i in da:
            app=app+str(i.id)+","
        if len(app)>1:
            app=app[0:len(app)-1]
        app+=")"
        sql += " or (approval in "+app+" and approval_type=2)"
    if len(orgAll)<1 and len(da)<1:
        count_2=0
    else:
        count_2 = len(OA_Reimbursement.query.filter(sql).all())
    return count_2