# coding:utf-8
from scapp.config import PER_PAGE
from scapp.config import logger
import scapp.helpers as helpers
from scapp import db,app
from scapp.models import OA_Project,OA_Customer,OA_Org,OA_User,OA_UserRole,OA_ProjectGroup
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


# 项目组管理
@app.route('/System/group', methods=['GET'])
def group():
    user = OA_User.query.order_by("id").all()
    return render_template("System/project/group.html",user=user)

#点击树生成右边列表
@app.route('/System/get_project_group/<type>/<int:p_id>', methods=['GET'])
def get_project_group(type,p_id):
    docs = OA_ProjectGroup.query.filter_by(type=type,project_id=p_id).all()
    for dos in docs:
        dos.real_name=dos.oa_project_group_ibfk_1.real_name
    return helpers.show_result_content(docs) # 返回json

#点击添加，生成默认以选中用户列表
@app.route('/System/get_user/<type>/<int:p_id>', methods=['GET'])
def get_user(type,p_id):
    docs = OA_ProjectGroup.query.filter_by(type=type,project_id=p_id).all()
    users= OA_User.query.order_by("id").all()
    for user in users:
        ifequal = 'false'
        for dos in docs:
            if dos.user_id==user.id:
                ifequal ='true'
        if ifequal=='true':
            user.checked = 'checked'
        else:
            user.checked = 'unchecked'
    return helpers.show_result_content(users) # 返回json

@app.route('/System/add/<type>/<int:p_id>/<value>', methods=['GET'])
def add(type,p_id,value):
    try:
        OA_ProjectGroup.query.filter_by(type=type,project_id=p_id).delete()
        ids = value.split(".")
        for i in ids:
            OA_ProjectGroup(p_id, type,i).add()
        user = OA_User.query.order_by("id").all()
        db.session.commit()
        # 消息闪现
        flash('保存成功','success')
    except:
        # 回滚
        db.session.rollback()
        logger.exception('exception')
        # 消息闪现
        flash('保存失败','error')
    return render_template("System/project/group.html",user=user)