# coding:utf-8

from flask import Module,request, render_template,flash,redirect
from flask.ext.login import login_user, logout_user, current_user, login_required
from scapp.models import OA_User
from scapp.models import OA_UserRole
from scapp.models import OA_Reimbursement

from scapp.config import logger
from scapp import app
from scapp import db

# 登陆
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = OA_User.query.filter_by(login_name=request.form['login_name'], login_password=request.form['login_password']).first()
        if user:
            login_user(user)
            role = OA_UserRole.query.filter_by(user_id=current_user.id).first().role
            level = role.role_level #取得用户权限等级

            status = 1
            count_1 = 0 #待上级审批
            count_2 = 0 #待您审批

            if level == 4 or level == 5:
                status = level - 1

            count_1=OA_Reimbursement.query.filter("create_user=:id","is_refuse=0","is_retreat=0","status!=5").params(id=current_user.id).count()
            count_2=OA_Reimbursement.query.filter("is_refuse=0","is_retreat=0","org_id=:department","status=:status","init_level<:role_level").params(department=current_user.department,status=status,role_level=level).count()

            return render_template("welcome.html",role=role,count_1=count_1,count_2=count_2)
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
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().role
    level = role.role_level #取得用户权限等级

    status = 1
    count_1 = 0 #待上级审批
    count_2 = 0 #待您审批

    if level == 4 or level == 5:
        status = level - 1

    count_1=OA_Reimbursement.query.filter("create_user=:id","is_refuse=0","is_retreat=0","status!=5").params(id=current_user.id).count()
    count_2=OA_Reimbursement.query.filter("is_refuse=0","is_retreat=0","org_id=:department","status=:status","init_level<:role_level").params(department=current_user.department,status=status,role_level=level).count()
    return render_template("welcome.html",role=role,count_1=count_1,count_2=count_2)

# 系统管理
@app.route('/xxgl', methods=['GET'])
@login_required
def xxgl():
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().role
    return render_template("index.html",menu = 'xxgl',role=role)

# 系统管理
@app.route('/xtgl', methods=['GET'])
@login_required
def xtgl():
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().role
    return render_template("index.html",menu = 'xtgl',role=role)

# 修改密码
@app.route('/change_password/<int:id>', methods=['GET','POST'])
def change_password(id):
    if request.method == 'POST':
        try:
            user = OA_User.query.filter_by(id=id).first()
            if user.login_password == request.form['old_password']:
                user.login_password = request.form['login_password']
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