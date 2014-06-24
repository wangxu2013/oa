# coding:utf-8
from scapp import db
from scapp.config import PER_PAGE
from scapp.config import logger
import scapp.helpers as helpers
import datetime

from flask import Module, session, request, render_template, redirect, url_for, flash
from flask.ext.login import current_user

from scapp.models import OA_Customer

from scapp import app

# 客户管理
@app.route('/System/customer/<int:page>', methods=['GET'])
def System_customer(page):
    customers = OA_Customer.query.order_by("id").paginate(page, per_page = PER_PAGE)
    return render_template("System/customer/customer.html",customers=customers)

# 新建
@app.route('/System/new_customer', methods=['GET','POST'])
def new_customer():
    if request.method == 'POST':
        try:
            OA_Customer(request.form['customer_name']).add()
            
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
        return redirect('System/customer/1')
    
    else:
        return render_template("System/customer/new_customer.html")

# 修改
@app.route('/System/edit_customer/<int:id>', methods=['GET','POST'])
def edit_customer(id):
    if request.method == 'POST':
        try:
            customer = OA_Customer.query.filter_by(id=id).first()
            customer.customer_name = request.form['customer_name']
            
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
        return redirect('System/customer/1')
    else:
        customer = OA_Customer.query.filter_by(id=id).first()
        return render_template("System/customer/edit_customer.html",customer=customer)