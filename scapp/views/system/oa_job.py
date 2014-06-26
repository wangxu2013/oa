# coding:utf-8
from scapp import db
from scapp.config import PER_PAGE
from scapp.config import logger
import scapp.helpers as helpers
import datetime

from flask import Module, session, request, render_template, redirect, url_for, flash
from flask.ext.login import current_user

from scapp.models import OA_Job

from scapp import app

# 职位管理
@app.route('/System/job/<int:page>', methods=['GET'])
def System_job(page):
    jobs = OA_Job.query.order_by("id").paginate(page, per_page = PER_PAGE)
    return render_template("System/job/job.html",jobs=jobs)

# 新建
@app.route('/System/new_job', methods=['GET','POST'])
def new_job():
    if request.method == 'POST':
        try:
            OA_Job(request.form['job_name']).add()
            
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
        return redirect('System/job/1')
    
    else:
        return render_template("System/job/new_job.html")

# 修改
@app.route('/System/edit_job/<int:id>', methods=['GET','POST'])
def edit_job(id):
    if request.method == 'POST':
        try:
            job = OA_Job.query.filter_by(id=id).first()
            job.job_name = request.form['job_name']
            
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
        return redirect('System/job/1')
    else:
        job = OA_Job.query.filter_by(id=id).first()
        return render_template("System/job/edit_job.html",job=job)