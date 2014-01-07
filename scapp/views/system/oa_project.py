# coding:utf-8
__author__ = 'johhny'

from scapp.config import logger
from scapp import db,app
from scapp.models import OA_Project,OA_Org
from flask import request,redirect,render_template,flash

#项目新增
@app.route('/system/project/add',methods=['GET','POST'])
def project_add():
    if request.method=='POST':
        try:
            OA_Project(request.form['project_num'],request.form['project_name'],
                       request.form['contract_num'],request.form['customer']
                       ,request.form['project_describe'],request.form['org_id']).add()
            db.session.commit()
            # 消息闪现
            flash('保存成功','success')
        except:
            # 回滚
            db.session.rollback()
            logger.exception('exception')
            # 消息闪现
            flash('保存失败','error')

        return redirect("system/project/add")

    else:

    	org = OA_Org.query.filter(OA_Org.id>1).all()
        return render_template('System/new_project.html',org=org)

