# coding:utf-8
import os
from scapp import db
from scapp.config import logger
import scapp.helpers as helpers
import datetime
import json
from flask import Module, session, request, render_template, redirect, url_for, flash
from flask.ext.login import current_user

from scapp.config import UPLOAD_FOLDER_REL
from scapp.config import UPLOAD_FOLDER_ABS

from scapp.models import OA_Project,OA_Reason,OA_Org,OA_User,OA_UserRole,OA_Reimbursement
from scapp.logic import recursion
from scapp.models import OA_Doc

from scapp import app

# 机构管理
@app.route('/wdgl/wdgl', methods=['GET'])
def wdgl():
    return render_template("wdgl/wdgl.html")

# 加载树
@app.route('/System/tree/doc/<int:id>', methods=['GET','POST'])
def doc_tree(id):
    orgs = OA_Org.query.filter_by(id=id).order_by("id").all()
    orgs_list = []
    if orgs:
        for obj in orgs:
            sql = "FIND_IN_SET(id ,getChildOrgLst('"+str(obj.id)+"'))"
            orgs_list += OA_Org.query.filter(sql).order_by("id").all()
    
    orgs_json = helpers.show_result_content(list(set(orgs_list)))
    orgs_json_obj = json.loads(orgs_json)
    
    for json_obj in orgs_json_obj:
        json_obj['type'] = "OA_Org"
        json_obj['icon'] = "/static/css/zTreeStyle/img/diy/1_open.png"
        projects = OA_Project.query.filter_by(p_org_id=json_obj["id"]).all()
        if projects:
            for pro_obj in projects:
                sql = "FIND_IN_SET(id ,getChildProjectLst('"+str(pro_obj.id)+"'))"
                projects_list = OA_Project.query.filter(sql).order_by("id").all()
                for objP in projects_list:
                    objP.name = objP.project_name
                    objP.type = "OA_Project"
                    objP.icon = "/static/css/zTreeStyle/img/diy/2.png"
                    
            json_obj['children'] = json.loads(helpers.show_result_content(projects))
        
    return json.dumps(orgs_json_obj)# 返回json

@app.route('/wdgl/get_project_docs/<type>/<int:p_id>', methods=['GET'])
def get_project_docs(type,p_id):
    if type == "OA_Org":
        docs = OA_Doc.query.filter_by(org_id=p_id).all()
    else:
        docs = OA_Doc.query.filter_by(project_id=p_id).all()
    return helpers.show_result_content(docs) # 返回json

# 下载
@app.route('/wdgl/download/<int:id>', methods=['GET'])
def download(id):
    doc = OA_Doc.query.filter_by(id=id).first()
    fname = doc.attachment
    if doc.org_id:
        dir = "OA_Org" + "_" +str(doc.org_id)
    else:
        dir = "OA_Project" + "_" +str(doc.project_id)
        
    #return send_from_directory(app.static_folder, 'upload/%d/%s' % (loan_apply_id,fname))
    return redirect(url_for('static', filename='upload/'+ dir + '/' + fname), code=301)

@app.route('/wdgl/new_doc/<type>/<int:p_id>', methods=['GET','POST'])
def new_doc(type,p_id):
    if request.method == 'POST':
        try:
            # 先获取上传文件
            f = request.files['attachment']
            fname = f.filename
            dir = type + "_" +str(p_id)
            if not os.path.exists(os.path.join(UPLOAD_FOLDER_ABS,dir)):
                os.mkdir(os.path.join(UPLOAD_FOLDER_ABS,dir))
            f.save(os.path.join(UPLOAD_FOLDER_ABS,'%s\\%s' % (dir,fname)))

            if type == "OA_Org":
                OA_Doc(request.form['name'],None,p_id,fname).add()
            else:
                OA_Doc(request.form['name'],p_id,None,fname).add()

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
            
        return render_template("wdgl/wdgl.html")
    else:
        print type
        return render_template("wdgl/new_wdgl.html",type=type,p_id=p_id)

@app.route('/wdgl/edit_doc/<int:id>', methods=['GET','POST'])
def edit_doc(id):
    doc = OA_Doc.query.filter_by(id=id).first()
    
    
    return render_template("wdgl/wdgl.html")