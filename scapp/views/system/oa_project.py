# coding:utf-8
from scapp.config import PER_PAGE
from scapp.config import logger
import scapp.helpers as helpers
from scapp import db,app
from scapp.models import OA_Project,OA_Customer,OA_Org,OA_User,OA_UserRole
from flask import request,redirect,render_template,flash

# 项目管理
@app.route('/System/project/<int:page>', methods=['GET'])
def System_project(page):
    projects = OA_Project.query.order_by("id").paginate(page, per_page = PER_PAGE)
    return render_template("System/project/project.html",projects=projects)

# 加载树
@app.route('/System/tree/OA_Project/<int:pid>', methods=['GET','POST'])
def init_project_tree(pid):
    tree = []
    roots = OA_Project.query.filter_by(p_org_id=pid).all()
    if roots:
        for obj in roots:
            sql = "FIND_IN_SET(id ,getChildProjectLst('"+str(obj.id)+"'))"
            tree += OA_Project.query.filter(sql).all()
    else:
        tree = None
        
    return helpers.show_result_content(list(set(tree))) # 返回json

#项目新增
@app.route('/System/new_project',methods=['GET','POST'])
def new_project():
    if request.method=='POST':
        try:
            if request.form['belong'] == '1':
                p_org_id = request.form['p_org_id']
                p_project_id = None
            else:
                p_org_id = None
                p_project_id = request.form['p_project_id']
                
            OA_Project(request.form['project_num'],request.form['project_name'],
                       request.form['contract_num'],request.form['project_describe'],
                       p_org_id,p_project_id,
                       request.form['customer_id']).add()
            db.session.commit()
            # 消息闪现
            flash('保存成功','success')
        except:
            # 回滚
            db.session.rollback()
            logger.exception('exception')
            # 消息闪现
            flash('保存失败','error')

        return redirect("System/project/1")

    else:
        orgs = OA_Org.query.filter(OA_Org.id>1).all()
        customers = OA_Customer.query.all()
        projects = OA_Project.query.all()
        user = OA_User.query.filter("id!=1").all()
        return render_template('System/project/new_project.html',orgs=orgs,user=user,customers=customers,projects=projects)
    
#项目修改
@app.route('/System/edit_project/<int:id>',methods=['GET','POST'])
def edit_project(id):
    if request.method=='POST':
        try:
            project = OA_Project.query.filter_by(id=id).first()
            project.project_num = request.form['project_num']
            project.project_name = request.form['project_name']
            project.contract_num = request.form['contract_num']
            project.project_describe = request.form['project_describe']
            
            if request.form['belong'] == '1':
                p_org_id = request.form['p_org_id']
                p_project_id = None
            else:
                p_org_id = None
                p_project_id = request.form['p_project_id']
                
            project.p_org_id = p_org_id
            project.p_project_id = p_project_id
            project.customer_id = request.form['customer_id']
            project.manager_id = request.form['manager_id']
            project.amount = request.form['amount']
            
            db.session.commit()
            # 消息闪现
            flash('保存成功','success')
        except:
            # 回滚
            db.session.rollback()
            logger.exception('exception')
            # 消息闪现
            flash('保存失败','error')

        return redirect("System/project/1")

    else:
        orgs = OA_Org.query.filter(OA_Org.id>1).all()
        customers = OA_Customer.query.all()
        projects = OA_Project.query.all()
        project = OA_Project.query.filter_by(id=id).first()
        user = OA_User.query.filter("id!=1").all()
        return render_template('System/project/edit_project.html',orgs=orgs,user=user,customers=customers,projects=projects,project=project)

