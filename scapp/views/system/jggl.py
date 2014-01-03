# coding:utf-8
from scapp import db
from scapp.config import logger
import scapp.helpers as helpers
import datetime

from flask import Module, session, request, render_template, redirect, url_for, flash
from flask.ext.login import current_user

from scapp.models import OA_Org

from scapp import app

# 机构管理
@app.route('/System/jggl', methods=['GET'])
def System_jggl():
    return render_template("System/jggl.html")

# 加载树
@app.route('/System/tree/<tablename>/<int:id>', methods=['GET','POST'])
def init_tree(tablename,id):
	# 加载所有
	if id == 0:
		tree = eval(tablename).query.order_by("id").all()

	# 加载对应id的子节点
	else:
		tree = eval(tablename).query.filter_by(pId=id).order_by("id").all()

	return helpers.show_result_content(tree) # 返回json
	
# 新增机构
@app.route('/System/new_jggl/<int:pId>', methods=['GET','POST'])
def new_jggl(pId):
	if request.method == 'POST':
		try:
			OA_Org(request.form['name'],pId).add()

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

		return redirect('System/jggl')
	else:
		return render_template("System/new_jggl.html",pId=pId)

# 新增机构
@app.route('/System/edit_jggl/<int:id>', methods=['GET','POST'])
def edit_jggl(id):
	if request.method == 'POST':
		try:
			obj = OA_Org.query.filter_by(id=id).first()
			obj.name = request.form['name']
			obj.modify_user = current_user.id
			obj.modify_date = datetime.datetime.now()
			
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

		return redirect('System/jggl')
	else:
		obj = OA_Org.query.filter_by(id=id).first()
		return render_template("System/edit_jggl.html",obj=obj)