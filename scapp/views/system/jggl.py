# coding:utf-8
from scapp import db
from scapp.config import logger
import scapp.helpers as helpers
import datetime

from flask import Module, session, request, render_template, redirect, url_for, flash
from flask.ext.login import current_user

from scapp.models import OA_Org
from scapp.models import OA_User

from scapp import app

# 机构管理
@app.route('/System/jggl', methods=['GET'])
def System_jggl():
    return render_template("System/org/jggl.html")

# 加载树
@app.route('/System/tree/OA_Org/<int:id>', methods=['GET','POST'])
def init_org_tree(id):
	# 加载所有
	if id == 0:
		tree = OA_Org.query.order_by("id").all()

	# 加载对应id的子节点
	else:
		tree = OA_Org.query.filter_by(pId=id).order_by("id").all()

	return helpers.show_result_content(tree) # 返回json
	
# 新增机构
@app.route('/System/new_jggl/<int:pId>', methods=['GET','POST'])
def new_jggl(pId):
	if request.method == 'POST':
		try:
			org_level = OA_Org.query.filter_by(id=pId).first().org_level + 1
			OA_Org(request.form['name'],pId,org_level).add()

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
		return render_template("System/org/new_jggl.html",pId=pId)

# 新增机构
@app.route('/System/edit_jggl/<int:id>', methods=['GET','POST'])
def edit_jggl(id):
    if request.method == 'POST':
        try:
            obj = OA_Org.query.filter_by(id=id).first()
            obj.name = request.form['name']
            obj.manager = request.form['manager']
            obj.amount = request.form['amount']
            obj.is_caiwu = request.form['is_caiwu']
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
        user = OA_User.query.filter("id!=1").all()
        return render_template("System/org/edit_jggl.html",obj=obj,user=user)
        
