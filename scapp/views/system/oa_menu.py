# coding:utf-8
from scapp import db
from scapp.config import logger
import scapp.helpers as helpers
import datetime

from flask import Module, session, request, render_template, redirect, url_for, flash
from flask.ext.login import current_user

from scapp.models import OA_Menu

from scapp import app

# 模块管理
@app.route('/System/menu', methods=['GET'])
def System_menu():
    return render_template("System/menu/menu.html")

# 加载树
@app.route('/System/tree/menu/<int:id>', methods=['GET','POST'])
def init_access_tree(id):
    # 加载所有
    if id == 0:
        tree = OA_Menu.query.order_by("id").all()
    else:
        tree = OA_Menu.query.filter_by(pid=id).order_by("id").all()
        
    return helpers.show_result_content(tree) # 返回json

# 新增模块或菜单
@app.route('/System/new_menu/<int:pId>', methods=['GET','POST'])
def new_menu(pId):
    if request.method == 'POST':
        try:
            menu = OA_Menu.query.filter_by(id=pId).first()
            OA_Menu(request.form['name'],request.form['menu_code'],pId,menu.level+1).add()

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

        return redirect('System/menu')
    else:
        return render_template("System/menu/new_menu.html",pId=pId)

# 编辑模块或菜单
@app.route('/System/edit_menu/<int:id>', methods=['GET','POST'])
def edit_menu(id):
    if request.method == 'POST':
        try:
            obj = OA_Menu.query.filter_by(id=id).first()
            obj.name = request.form['name']
            obj.menu_code = request.form['menu_code']

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

        return redirect('System/menu')
    else:
        obj = OA_Menu.query.filter_by(id=id).first()
        return render_template("System/menu/edit_menu.html",obj=obj)
            
# 删除模块或菜单
@app.route('/System/delete_menu/<int:id>', methods=['GET','POST'])
def delete_menu(id):
    try:
        OA_Menu.query.filter_by(id=id).delete()

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

    return redirect('System/menu')