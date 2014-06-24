# coding:utf-8
from scapp import db
from scapp.config import PER_PAGE
from scapp.config import logger
import scapp.helpers as helpers
import datetime

from flask import Module, session, request, render_template, redirect, url_for, flash
from flask.ext.login import current_user

from scapp.models import OA_Reason

from scapp import app

# 事由管理
@app.route('/System/reason/<int:page>', methods=['GET'])
def System_reason(page):
    reasons = OA_Reason.query.order_by("id").paginate(page, per_page = PER_PAGE)
    return render_template("System/reason/reason.html",reasons=reasons)

# 新建
@app.route('/System/new_reason', methods=['GET','POST'])
def new_reason():
    if request.method == 'POST':
        try:
            OA_Reason(request.form['reason_name']).add()
            
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
        return redirect('System/reason/1')
    
    else:
        return render_template("System/reason/new_reason.html")

# 修改
@app.route('/System/edit_reason/<int:id>', methods=['GET','POST'])
def edit_reason(id):
    if request.method == 'POST':
        try:
            reason = OA_Reason.query.filter_by(id=id).first()
            reason.reason_name = request.form['reason_name']
            
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
        return redirect('System/reason/1')
    else:
        reason = OA_Reason.query.filter_by(id=id).first()
        return render_template("System/reason/edit_reason.html",reason=reason)
    
    