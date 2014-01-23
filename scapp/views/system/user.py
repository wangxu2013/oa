# coding:utf-8
from scapp import db
from scapp.config import PER_PAGE
from scapp.config import logger
import datetime

from flask import Module, session, request, render_template, redirect, url_for, flash
from flask.ext.login import current_user

from scapp.models import OA_User
from scapp.models import OA_Role
from scapp.models import OA_UserRole
from scapp.models import OA_Org

from scapp import app

# 使用者管理
@app.route('/System/syzgl/<int:page>', methods=['GET'])
def System_syzgl(page):
	users = OA_User.query.order_by("id").paginate(page, per_page = PER_PAGE)
	return render_template("System/syzgl.html",users=users)
	
# 新增用户
@app.route('/System/new_user', methods=['GET','POST'])
def new_user():
	if request.method == 'GET':
		roles = OA_Role.query.order_by("id").all()
		orgs = OA_Org.query.filter("id>1").order_by("id").all()
		return render_template("System/new_user.html",roles=roles,orgs=orgs)
	else:
		try:
			user = OA_User(request.form['login_name'],request.form['login_password'],
				request.form['real_name'],request.form['sex'],request.form['mobile'],
				request.form['department'],request.form['active'])
			user.add()

			#清理缓存
			db.session.flush()

			OA_UserRole(user.id,request.form['roles']).add()

			# 事务提交
			db.session.commit()
			# 消息闪现
			flash('保存成功','success')
		except:
			# 回滚
			db.session.rollback()
			logger.exception('exception')
			# 消息闪现
			flash('保存失败','error')

		return redirect('System/syzgl/1')

# 编辑用户
@app.route('/System/edit_user/<int:id>', methods=['GET','POST'])
def edit_user(id):
	if request.method == 'GET':
		user = OA_User.query.filter_by(id=id).first()
		roles = OA_Role.query.order_by("id").all()
		role = OA_UserRole.query.filter_by(user_id=id).first().role
		orgs = OA_Org.query.filter("id>1").order_by("id").all()
		return render_template("System/edit_user.html",user=user,roles=roles,role=role,orgs=orgs)
	else:
		try:
			user = OA_User.query.filter_by(id=id).first()
			user.login_name = request.form['login_name']
			#user.login_password = request.form['login_password']
			user.real_name = request.form['real_name']
			user.sex = request.form['sex']
			user.mobile = request.form['mobile']
			user.department = request.form['department']
			user.active = request.form['active']
			user.modify_user = current_user.id
			user.modify_date = datetime.datetime.now()

			user_role = OA_UserRole.query.filter_by(user_id=id).first()
			user_role.role_id = request.form['roles']
			user_role.modify_user = current_user.id
			user_role.modify_date = datetime.datetime.now()

			# 事务提交
			db.session.commit()
			# 消息闪现
			flash('保存成功','success')
		except:
			# 回滚
			db.session.rollback()
			logger.exception('exception')
			# 消息闪现
			flash('保存失败','error')

		return redirect('System/syzgl/1')

# 角色权限管理
@app.route('/System/jsqxgl/<int:page>', methods=['GET'])
def System_jsqxgl(page):
    # 获取角色并分页
    roles = OA_Role.query.order_by("id").paginate(page, per_page = PER_PAGE)
    return render_template("System/jsqxgl.html",roles = roles)

# 新增角色
@app.route('/System/new_role', methods=['GET','POST'])
def new_role():
	if request.method == 'POST':
		try:
			# 保存角色
			role = OA_Role(request.form['role_name'], request.form['role_level'])
			role.add()

			# 事务提交
			db.session.commit()
			# 消息闪现
			flash('保存成功','success')
		except:
			# 回滚
			db.session.rollback()
			logger.exception('exception')
			# 消息闪现
			flash('保存失败','error')

		return redirect('System/jsqxgl/1')

	elif request.method == 'GET':
		return render_template("System/new_role.html")

# 更新角色
@app.route('/System/edit_role/<int:id>', methods=['GET','POST'])
def edit_role(id):
	if request.method == 'POST':
		try:
			OA_Role.query.filter_by(id=id).update({"role_name":request.form['role_name'],"role_level":request.form['role_level']})
			
			# 事务提交
			db.session.commit()
			# 消息闪现
			flash('保存成功','success')
		except:
			# 回滚
			db.session.rollback()
			logger.exception('exception')
			# 消息闪现
			flash('保存失败','error')

		return redirect('System/jsqxgl/1')

	elif request.method == 'GET':
		role = OA_Role.query.filter_by(id=id).first()

		return render_template("System/edit_role.html",role=role)