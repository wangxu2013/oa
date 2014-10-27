# coding:utf-8
import os
from scapp import db
from scapp.config import PER_PAGE
from scapp.config import logger
import scapp.helpers as helpers
import datetime
import json
from flask import Module, session, request, render_template, redirect, url_for, flash
from flask.ext.login import current_user

from scapp.config import UPLOAD_FOLDER_REL
from scapp.config import UPLOAD_FOLDER_ABS

from scapp.models import OA_Project,OA_Reason,OA_Org,OA_User,OA_UserRole,OA_Reimbursement,OA_Privilege,OA_View_Doc_Privilege,OA_ProjectGroup
from scapp.logic import recursion
from scapp.models import OA_Doc,OA_Doc_Version

from scapp import app
import shutil


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
        projects = OA_Project.query.filter("p_org_id="+str(json_obj["id"])+" and treeType<>2").all()
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
        docs = OA_View_Doc_Privilege.query.filter("org_id="+str(p_id)+" and privilege_master_id="+str(current_user.id)+" LIMIT 0,10").all()
    else:
        docs = OA_View_Doc_Privilege.query.filter("project_id="+str(p_id)+" and privilege_master_id="+str(current_user.id)+" LIMIT 0,10").all()
    return helpers.show_result_content(docs) # 返回json

@app.route('/wdgl/get_doc_version/<int:id>', methods=['GET'])
def get_doc_version(id):
    doc = OA_Doc.query.filter_by(id=id).first()
    doc_version = OA_Doc_Version.query.filter_by(doc_id=id).order_by("version").all()
    for obj in doc_version:
        obj.create_user = doc.create_user
    return helpers.show_result_content(doc_version) # 返回json

# 下载
@app.route('/wdgl/download/<int:version>/<int:id>', methods=['GET'])
def wdgl_download(version,id):
    oa_doc = OA_Doc.query.filter_by(id=id).first()
    if version == 0:
        doc_versions = OA_Doc_Version.query.filter_by(doc_id=id).all()
        version = doc_versions[len(doc_versions)-1].version
    if oa_doc.org_id:
        dir_version = "OA_Org" + "_" +str(oa_doc.org_id)+"/"+str(id)+"_"+str(version)
    else:
        dir_version = "OA_Project" + "_" +str(oa_doc.project_id)+"/"+str(id)+"_"+str(version)
    
    doc_version = OA_Doc_Version.query.filter_by(doc_id=id,version=version).first()
    return redirect(url_for('static', filename='upload/'+ dir_version + '/' + doc_version.attachment), code=301)

# 删除
@app.route('/wdgl/delete/<int:id>', methods=['GET'])
def wdgl_delete(id):
    try:
        oa_doc = OA_Doc.query.filter_by(id=id).first()
        doc_versions = OA_Doc_Version.query.filter_by(doc_id=id).all()
        #删除db
        OA_Doc.query.filter_by(id=id).delete()
        db.session.flush()
        #删权限
        OA_Privilege.query.filter_by(privilege_access="OA_Doc",privilege_access_value=id).delete()
        db.session.flush()
        #删文件
        for obj in doc_versions:
            if oa_doc.org_id:
                dir_version = "OA_Org" + "_" +str(oa_doc.org_id)+"/"+str(id)+"_"+str(obj.version)
            else:
                dir_version = "OA_Project" + "_" +str(oa_doc.project_id)+"/"+str(id)+"_"+str(obj.version)
            shutil.rmtree(os.path.join(UPLOAD_FOLDER_ABS,dir_version))
        
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

@app.route('/wdgl/check_new_privilege/<type>/<int:p_id>', methods=['GET'])
def check_new_privilege(type,p_id):
    prv = OA_ProjectGroup.query.filter_by(type=type,project_id=p_id,user_id=current_user.id).all()
    if prv:
        return helpers.show_result_success("Success")
    else:
        return helpers.show_result_fail("Failed")
    
@app.route('/wdgl/new_doc/<type>/<int:p_id>', methods=['GET','POST'])
def new_doc(type,p_id):
    if request.method == 'POST':
        try:
            # 获取上传文件
            f = request.files['attachment']
            fname = f.filename
            
            #先存db
            #主表
            if type == "OA_Org":
                oa_doc = OA_Doc(request.form['name'],None,p_id,fname)    
            else:
                oa_doc = OA_Doc(request.form['name'],p_id,None,fname)
            oa_doc.add()
            db.session.flush()
            
            #子表
            OA_Doc_Version(oa_doc.id,1,fname).add()
            
            #再操作硬盘
            #创建主文件夹
            dir = type + "_" +str(p_id)
            if not os.path.exists(os.path.join(UPLOAD_FOLDER_ABS,dir)):
                os.mkdir(os.path.join(UPLOAD_FOLDER_ABS,dir))
            #创建版本子文件夹
            dir_version = type + "_" +str(p_id)+"/"+str(oa_doc.id)+"_1"
            if not os.path.exists(os.path.join(UPLOAD_FOLDER_ABS,dir_version)):
                os.mkdir(os.path.join(UPLOAD_FOLDER_ABS,dir_version))
            #上传
            f.save(os.path.join(UPLOAD_FOLDER_ABS,'%s/%s' % (dir_version,fname)))
            
            #存权限
            user_id_ls = request.form.getlist("user_id")
            for obj in user_id_ls:
                privilege_tmp = request.form.getlist('privilege_'+obj)
                tmp_sum = 0
                for tmp in privilege_tmp:
                    tmp_sum += int(tmp)
                if tmp_sum >0:
                    OA_Privilege("OA_User",obj,"OA_Doc",oa_doc.id,tmp_sum).add()
                    
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
            
        return render_template("wdgl/wdgl.html",type=type,p_id=p_id,second=1)
    else:
        user= OA_User.query.filter("active='1'").order_by("id").all()
        user_group = OA_User.query.filter("id in (select user_id from oa_project_group where type='"+type+"' and project_id="+str(p_id)+")").all()
        return render_template("wdgl/new_wdgl.html",type=type,p_id=p_id,user=user,user_group=user_group)

#进入文件权限更新页面
@app.route('/wdgl/edit_doc/<int:docId>/<type>/<int:p_id>', methods=['GET','POST'])
def edit_doc(docId,type,p_id):
    if request.method == 'GET':
        doc = OA_Doc.query.filter_by(id=docId).first()
        #user= OA_User.query.filter("active='1' and id<>1").order_by("id").all()
        #privileges = OA_Privilege.query.filter("privilege_access='OA_Doc' and privilege_access_value="+str(docId)).order_by("privilege_master_id").all()
        #调用存储过程
        user_doc_privilege = db.session.execute("call pro_user_doc_privilege("+str(docId)+")").fetchall()
        return render_template("wdgl/edit_wdgl.html",doc=doc,user_doc_privilege=user_doc_privilege,type=type,p_id=p_id)  
    else:
        try:
            oa_doc = OA_Doc.query.filter_by(id=docId).first()
            # 先获取上传文件
            f = request.files['attachment']
            if f:#更新文件
                fname = f.filename
                
                oa_doc.name=request.form['name']
                oa_doc.attachment=fname
                    
                #获取已有的版本
                doc_versions = OA_Doc_Version.query.filter_by(doc_id=docId).order_by("version").all()
                
                #创建最新的
                max_doc=doc_versions[len(doc_versions)-1]
                cur_version = max_doc.version+1
                
                #存db
                #子表
                OA_Doc_Version(oa_doc.id,cur_version,fname).add()
                
                #操作硬盘
                #创建版本子文件夹
                if oa_doc.org_id:
                    dir_version = "OA_Org" + "_" +str(oa_doc.org_id)+"/"+str(oa_doc.id)+"_"+str(cur_version)
                else:
                    dir_version = "OA_Project" + "_" +str(oa_doc.project_id)+"/"+str(oa_doc.id)+"_"+str(cur_version)
                if not os.path.exists(os.path.join(UPLOAD_FOLDER_ABS,dir_version)):
                    os.mkdir(os.path.join(UPLOAD_FOLDER_ABS,dir_version))
                #上传
                f.save(os.path.join(UPLOAD_FOLDER_ABS,'%s/%s' % (dir_version,fname)))
                
                #更新版本子表
                if len(doc_versions) == 5:#之前已有5个版本
                    #删除最老的
                    min_doc = doc_versions[0]
                    #删除最老的版本记录
                    OA_Doc_Version.query.filter_by(doc_id=docId,version=min_doc.version).delete()
                    
                    shutil.rmtree(os.path.join(UPLOAD_FOLDER_ABS,'%s/%s' % ("OA_Org" + "_" +str(oa_doc.org_id),str(oa_doc.id)+'_'+str(min_doc.version))))
                    
            else:#不更新文件
                oa_doc.name=request.form['name']
            
            #删除旧权限
            OA_Privilege.query.filter_by(privilege_access="OA_Doc",privilege_access_value=oa_doc.id).delete()
            db.session.flush()
            #存权限
            user_id_ls = request.form.getlist("user_id")
            for obj in user_id_ls:
                privilege_tmp = request.form.getlist('privilege_'+obj)
                tmp_sum = 0
                for tmp in privilege_tmp:
                    tmp_sum += int(tmp)
                if tmp_sum >0:
                    OA_Privilege("OA_User",obj,"OA_Doc",oa_doc.id,tmp_sum).add()
                    
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
            
        return render_template("wdgl/wdgl.html",type=type,p_id=p_id,second=1)

# #分页查询
@app.route('/wdgl/information/<type>/<int:p_id>/<int:page>', methods=['GET'])
def information(type,p_id,page):
    page_count = str((page-1)*PER_PAGE)+","+str(page*PER_PAGE)
    docs = ""
    if type == "OA_Org":
        docs = OA_View_Doc_Privilege.query.filter("org_id="+str(p_id)+" and (privilege_master_id="+str(current_user.id)+") LIMIT "+page_count).all()
        lenth = len(OA_View_Doc_Privilege.query.filter("org_id="+str(p_id)+" and (privilege_master_id="+str(current_user.id)+")").all())
        if int(lenth%10)==0:
            pages = lenth/10
        else:
            pages = lenth/10+1
    else:
        docs = OA_View_Doc_Privilege.query.filter("project_id="+str(p_id)+" and (privilege_master_id="+str(current_user.id)+") LIMIT "+page_count).all()
        lenth = len(OA_View_Doc_Privilege.query.filter("project_id="+str(p_id)+" and (privilege_master_id="+str(current_user.id)+")").all())
        if int(lenth%10)==0:
            pages = lenth/10
        else:
            pages = lenth/10+1
    for doc in docs:
        doc.pages =pages
        doc.page = page
    return helpers.show_result_content(docs)