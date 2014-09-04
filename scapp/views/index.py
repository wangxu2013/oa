# coding:utf-8

from flask import Module,request, render_template,flash,redirect
from flask.ext.login import login_user, logout_user, current_user, login_required
from scapp.models import OA_Org,OA_Project,OA_Task_Main,OA_Task_User,OA_Task_Board
from scapp.models import OA_User
from scapp.models import OA_UserRole
from scapp.models import OA_Reimbursement
from scapp.models import OA_Privilege
from scapp.logic.reimbursement import costs_statistics
from scapp.config import logger
from scapp import app
from scapp import db
from scapp.tools.flash_pic import flash_pic

import hashlib
import datetime
#get md5 of a input string  
def GetStringMD5(str):  
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest() 
	
# 登陆
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = OA_User.query.filter_by(login_name=request.form['login_name'], login_password=GetStringMD5(request.form['login_password'])).first()
        if user:
            login_user(user)
            role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
            privileges = OA_Privilege.query.filter_by(privilege_master="OA_Role",privilege_master_id=role.id,privilege_access="OA_Menu").all()
            
            count_1=len(OA_Reimbursement.query.filter_by(create_user=current_user.id,is_paid=0).all())
            count_2=getCount()
            
            orgs = OA_Org.query.filter_by(manager=current_user.id).all()
            result = []
            for obj in orgs:
                tmp = {}
                tmp["name"] = obj.name
                tmp["total_apply"]=costs_statistics.get_total_apply_costs(obj.id)
                tmp["total_paid"]=costs_statistics.get_total_paid_costs(obj.id)
                tmp["monthly"]=costs_statistics.get_monthly_paid_costs(obj.id)
                tmp["season"]=costs_statistics.get_season_paid_costs(obj.id)
                result.append(tmp)
                
            return render_template("welcome.html",role=role,count_1=count_1,count_2=count_2,result=result,privileges=privileges)
        else:
            flash('用户名或密码错误','error')
            return render_template("login.html")

    else:
        return render_template("login.html")

# 注销
@app.route('/logout')
def logout():
    logout_user()
    return render_template("login.html")
    
# 欢迎界面
@app.route('/welcome', methods=['GET'])
@login_required
def welcome():
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
    privileges = OA_Privilege.query.filter_by(privilege_master="OA_Role",privilege_master_id=role.id,privilege_access="OA_Menu").all()
    
    count_1=len(OA_Reimbursement.query.filter_by(create_user=current_user.id,is_paid=0).all())
    count_2=getCount()
    
    orgs = OA_Org.query.filter_by(manager=current_user.id).all()
    result = []
    for obj in orgs:
        tmp = {}
        tmp["name"] = obj.name
        tmp["total_apply"]=costs_statistics.get_total_apply_costs(obj.id)
        tmp["total_paid"]=costs_statistics.get_total_paid_costs(obj.id)
        tmp["monthly"]=costs_statistics.get_monthly_paid_costs(obj.id)
        tmp["season"]=costs_statistics.get_season_paid_costs(obj.id)
        result.append(tmp)
                
    return render_template("welcome.html",role=role,count_1=count_1,count_2=count_2,result=result,privileges=privileges)

# 系统管理
@app.route('/xxgl', methods=['GET'])
@login_required
def xxgl():
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
    privileges = OA_Privilege.query.filter_by(privilege_master="OA_Role",privilege_master_id=role.id,privilege_access="OA_Menu").all()
    return render_template("index.html",menu = 'xxgl',role=role,privileges=privileges,userId=current_user.id)

# 文档管理
@app.route('/Wdgl', methods=['GET'])
@login_required
def Wdgl():
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
    privileges = OA_Privilege.query.filter_by(privilege_master="OA_Role",privilege_master_id=role.id,privilege_access="OA_Menu").all()
    return render_template("index.html",menu = 'Wdgl',role=role,privileges=privileges)
	
# 统计报表
@app.route('/xmgl', methods=['GET'])
@login_required
def Xmgl():
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
    privileges = OA_Privilege.query.filter_by(privilege_master="OA_Role",privilege_master_id=role.id,privilege_access="OA_Menu").all()
    return render_template("index.html",menu = 'xmgl',role=role,privileges=privileges)
	
# 统计报表
@app.route('/Tjbb', methods=['GET'])
@login_required
def Tjbb():
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
    privileges = OA_Privilege.query.filter_by(privilege_master="OA_Role",privilege_master_id=role.id,privilege_access="OA_Menu").all()
    return render_template("index.html",menu = 'Tjbb',role=role,privileges=privileges)

# 系统管理
@app.route('/xtgl', methods=['GET'])
@login_required
def xtgl():
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
    privileges = OA_Privilege.query.filter_by(privilege_master="OA_Role",privilege_master_id=role.id,privilege_access="OA_Menu").all()
    return render_template("index.html",menu = 'xtgl',role=role,privileges=privileges)

# 待审批
@app.route('/dsp', methods=['GET'])
@login_required
def dsp():
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().oa_userrole_ibfk_2
    privileges = OA_Privilege.query.filter_by(privilege_master="OA_Role",privilege_master_id=role.id,privilege_access="OA_Menu").all()
    return render_template("index.html",menu = 'dsp',role=role,privileges=privileges)

# 修改密码
@app.route('/change_password/<int:id>', methods=['GET','POST'])
def change_password(id):
    if request.method == 'POST':
        try:
            user = OA_User.query.filter_by(id=id).first()
            if user.login_password == GetStringMD5(request.form['old_password']):
                user.login_password = GetStringMD5(request.form['login_password'])
            else:
                raise Exception

            # 事务提交
            db.session.commit()
            # 消息闪现
            flash('修改密码成功，请重新登录！','success')

        except:
            # 回滚
            db.session.rollback()
            logger.exception('exception')
            # 消息闪现
            flash('修改密码失败，为保障安全，请重新登录后再尝试修改！','error')

        logout_user()
        return redirect("login")
    else:
        return render_template("change_password.html")

#首页获取待审核项目数
def getCount():
    count_2=0
    #查询待审批
    sql =" is_paid=0 and is_refuse=0 "
    if current_user.id is not 15:
        sql+=" and approval_type!=4 "
    orgAll = OA_Org.query.filter_by(manager=current_user.id).all()
    sql+=" and ("
    if len(orgAll)>0:
        appreval ="("
        #判断是否含有财务部门
        type ='1'
        for i in orgAll:
            appreval=appreval+str(i.id)+","
            if i.is_caiwu==1:
                type='2'
        if len(appreval)>1:
            appreval=appreval[0:len(appreval)-1]
        appreval+=")"
        sql += " (approval in "+appreval
        #含财务部门
        if type=='2':
            sql += " or approval_type = 3)"
        else:
            sql += " and approval_type=1)"
    else:
       sql +=" approval is null" 
    da = OA_Project.query.filter_by(manager_id=current_user.id).all()
    if len(da)>0:
        app ="("
        for i in da:
            app=app+str(i.id)+","
        if len(app)>1:
            app=app[0:len(app)-1]
        app+=")"
        sql += " or (approval in "+app+" and approval_type=2)"
    if len(orgAll)<1 and len(da)<1:
        count_2=0
    else:
        if current_user.id==15:
            sql +=" or (approval_type=4 and is_paid=0)"
        sql+=")"
        sql+=" GROUP BY create_user"
        data = db.session.execute("select a.create_user,(select real_name from oa_user b where b.id=a.create_user) as real_name,sum(a.amount) as amount from oa_reimbursement a where "+sql).fetchall()
        count_2=len(data)
    return count_2
		
# 项目管理-个人项目
@app.route('/xmgl/grxm', methods=['GET','POST'])
def grxm():
    data = OA_Task_User.query.filter_by(user_id=current_user.id).order_by("id desc").all()
    return render_template("xmgl/grxm.html",data=data,user_id=current_user.id)	

# 项目管理-新增页面
@app.route('/xmgl/new_xm', methods=['GET'])
def new_xm():
    return render_template("xmgl/new_xm.html")  

# 项目管理-新增
@app.route('/xmgl/create', methods=['POST'])
def create():
    try:
        task_name = request.form['task_name']
        task_content = request.form['task_content']
        main = OA_Task_Main(task_name,task_content)
        main.add()
        db.session.flush()
        OA_Task_User(current_user.id,main.id).add()
        # 事务提交
        db.session.commit()
    except:
        # 回滚
        db.session.rollback()
        logger.exception('exception')
    return ""

# 项目管理-编辑项目
@app.route('/xmgl/edit_xm/<int:id>', methods=['GET'])
def edit_xm(id):
    data = OA_Task_Main.query.filter_by(id=id).first()
    return render_template("xmgl/edit_xm.html",data=data)

# 项目管理-编辑
@app.route('/xmgl/edit', methods=['POST'])
def edit():
    try:
        task_id = request.form['task_id']
        task_name = request.form['task_name']
        task_content = request.form['task_content']
        data = OA_Task_Main.query.filter_by(id=task_id).first()
        data.subject= task_name
        data.content= task_content
        # 事务提交
        db.session.commit()
    except:
        # 回滚
        db.session.rollback()
        logger.exception('exception')
    return ""

# 项目管理-关闭
@app.route('/xmgl/close/<int:id>', methods=['POST'])
def close(id):
    try:
        data = OA_Task_Main.query.filter_by(id=id).first()
        data.delete= 1
        # 事务提交
        db.session.commit()
        # flash('关闭成功！','success')
    except:
        # 回滚
        db.session.rollback()
        logger.exception('exception')
        # flash('关闭失败！','false')
    return redirect("/xmgl/grxm")
	
# 项目管理-项目信息
@app.route('/xmgl/xmxx/<int:task_id>', methods=['GET'])
def xmxx(task_id):
    data = OA_Task_Main.query.filter_by(id=task_id).first()
    if int(data.create_user) is not int(current_user.id):
        create = "false"
    else:
        create = "true"
    #项目成员
    task_user = OA_Task_User.query.filter_by(task_id=task_id).all()
    #任务列表
    sql = "static!=3 and task_id="+str(task_id)+" and user_id="+str(current_user.id)
    task_board = OA_Task_Board.query.filter(sql).order_by("finish_time").all()
    #已完成
    list_1 = OA_Task_Board.query.filter("static='3' and task_id="+str(task_id)).count()
    #当日待完成
    date = datetime.datetime.now().date().strftime("%Y-%m-%d")
    list_2 = OA_Task_Board.query.filter("static!='3' and task_id="+str(task_id)+" and substring(finish_time,1,10)='"+date+"'").count()
    #任务总数
    list_3 = OA_Task_Board.query.filter("static!='3' and task_id="+str(task_id)).count()
    return render_template("xmgl/xmxx.html",task_user=task_user,task_id=task_id,create=create,task_board=task_board,\
        list_1=list_1,list_2=list_2,list_3=list_3,data=data)
		
# 项目管理-任务板
@app.route('/xmgl/rwb/<int:task_id>', methods=['GET'])
def rwb(task_id):
    #任务列表
    sql = "task_id="+str(task_id)+" and user_id="+str(current_user.id)
    task_board = OA_Task_Board.query.filter(sql).order_by("finish_time").all()
    task = OA_Task_Main.query.filter_by(id=task_id).first()
    return render_template("xmgl/rwb.html",task_board=task_board,task_id=task_id,task=task,task_type="true")

# 项目管理-其它成员任务板
@app.route('/xmgl/otherRwb/<int:task_id>/<int:user_id>', methods=['GET'])
def otherRwb(task_id,user_id):
    #任务列表
    sql = "task_id="+str(task_id)+" and user_id="+str(user_id)
    task_board = OA_Task_Board.query.filter(sql).order_by("finish_time").all()
    task = OA_Task_Main.query.filter_by(id=task_id).first()
    if user_id is not current_user.id:
        task_type="false"
    return render_template("xmgl/rwb.html",task_board=task_board,task_id=task_id,task=task,task_type="false")

# 项目管理-任务板状态变化
@app.route('/xmgl/rwbStatic/<int:id>', methods=['GET'])
def rwbStatic(id):
    try:
        data = OA_Task_Board.query.filter_by(id=id).first()
        if str(data.static) is not '3':
            data.static = int(data.static)+1
            if str(data.static)=='3':
                data.end_time=datetime.datetime.now()
        else:
            data.static = "2"
        db.session.commit()
    except:
        # 回滚
        db.session.rollback()
        logger.exception('exception')
    return ""
	
# 项目管理-新增任务
@app.route('/xmgl/new_rw/<int:task_id>', methods=['GET'])
def new_rw(task_id):
    users = OA_Task_User.query.filter_by(task_id=task_id).all()
    task = OA_Task_Main.query.filter_by(id=task_id).first()
    return render_template("xmgl/new_rw.html",task_id=task_id,users=users,task=task)

# 项目管理-新增任务保存
@app.route('/xmgl/new_rw_over/<int:task_id>', methods=['POST'])
def new_rw_over(task_id):
    try:
        task_content = request.form['task_content']
        task_user = request.form['task_user']
        finish_time = request.form['finish_time']
        OA_Task_Board(task_user,task_id,task_content,finish_time,"1",request.form['finish_time']).add()
        # 事务提交
        db.session.commit()
        # flash('新增成功！','success')
    except:
        # 回滚
        db.session.rollback()
        logger.exception('exception')
        # flash('新增失败！','false')

    return redirect("/xmgl/xmxx/"+str(task_id))
	
# 项目管理-编辑任务
@app.route('/xmgl/edit_rw', methods=['GET'])
def edit_rw():
    return render_template("xmgl/edit_rw.html")
	
# 项目管理-添加组员
@app.route('/xmgl/add_zy/<int:task_id>', methods=['GET'])
def add_zy(task_id):
    sql = "select a.id,a.real_name,a.login_name,b.user_id from (select * from  oa_user where id!="+str(current_user.id)+") as a  LEFT JOIN oa_task_user b on a.id=b.user_id and b.task_id="+str(task_id)
    data = db.session.execute(sql).fetchall()
    task = OA_Task_Main.query.filter_by(id=task_id).first()
    return render_template("xmgl/add_zy.html",data=data,task_id=task_id,task=task)

# 项目管理-添加
@app.route('/xmgl/add_zy_over/<int:task_id>/<users>', methods=['POST'])
def add_zy_over(task_id,users):
    try:
        sql ="task_id="+str(task_id)+" and user_id!="+str(current_user.id)
        OA_Task_User.query.filter(sql).delete(synchronize_session=False)
        db.session.flush()
        if "." in users:
            value=users.split(".")
            for obj in value:
                OA_Task_User(obj,task_id).add()
        else:
            value=users
            OA_Task_User(value,task_id).add()
        db.session.commit()
    except:
        # 回滚
        db.session.rollback()
        logger.exception('exception')
    return redirect("/xmgl/xmxx/"+str(task_id))

	
# 项目管理-未完成任务
@app.route('/xmgl/unfinish/<task_id>', methods=['GET'])
def unfinish(task_id):
    data = OA_Task_Board.query.filter("static!='3' and task_id="+str(task_id)).order_by("finish_time").all()
    task = OA_Task_Main.query.filter_by(id=task_id).first()
    return render_template("xmgl/unfinish.html",data=data,task_id=task_id,task=task)
	
# 项目管理-已完成任务
@app.route('/xmgl/finish/<task_id>', methods=['GET'])
def finish(task_id):
    data = OA_Task_Board.query.filter("static='3' and task_id="+str(task_id)).order_by("end_time desc").all()
    task = OA_Task_Main.query.filter_by(id=task_id).first()
    return render_template("xmgl/finish.html",data=data,task_id=task_id,task=task)
	
# 项目管理-今日任务
@app.route('/xmgl/today/<task_id>', methods=['GET'])
def today(task_id):
    date = datetime.datetime.now().date().strftime("%Y-%m-%d")
    data = OA_Task_Board.query.filter("static!=3 and task_id="+str(task_id)+" and substring(finish_time,1,10)='"+date+"'").all()
    task = OA_Task_Main.query.filter_by(id=task_id).first()
    return render_template("xmgl/today.html",data=data,task_id=task_id,task=task)
			
# 项目管理-管理项目
@app.route('/xmgl/glxm', methods=['GET','POST'])
def glxm():
    data = get_recursion_project(current_user.id)
    return render_template("xmgl/glxm.html",data=data,user_id=current_user.id)	
			
# 项目管理-项目搜索页面
@app.route('/xmgl/xm_search', methods=['GET','POST'])
def xm_search():
    org = OA_Org.query.filter_by(manager=current_user.id).first()
    data = ''
    if org:
        data = get_recursion_org(org.id)
    return render_template("xmgl/xm_search.html",data=data,user_id=current_user.id)	

# 项目管理-查询项目结果
@app.route('/xmgl/glxm_result/<org_id>/<task_name>', methods=['GET','POST'])
def glxm_result(org_id,task_name):
    data = get_recursion_project_task(org_id,task_name)
    return render_template("xmgl/glxm.html",data=data,user_id=current_user.id)  
	
	
# 统计报表-年度费用统计搜索
@app.route('/tjbb/ndfytj_search', methods=['GET'])
def ndfytj_search():
    if str(current_user.id) == '1':
        data = OA_Org.query.all()
    else:
        data = OA_Org.query.filter_by(manager=current_user.id).all()
        if data[0].org_level==0:
            data = OA_Org.query.filter("pid=1").all()
    return render_template("tjbb/ndfytj_search.html",data=data)
	
# 统计报表-年度费用统计
@app.route('/tjbb/ndfytj', methods=['POST'])
def ndfytj():
    org = request.form['org']
    time = request.form['time']
    return render_template("tjbb/ndfytj.html",org=org,time=time)

# 柱状图
@app.route('/Report/create/bar_3d/<org>/<time>', methods=['GET'])
def Report_create_bar_3d(org,time):
    exp = flash_pic()
    sql = "SELECT concat(b.month,'月') AS MONTH,IFNULL(a.amount,0) FROM oa_month b LEFT JOIN \
    (SELECT SUBSTR(create_date, 6, 2) as create_date, IFNULL(SUM(amount), 0) AS amount FROM oa_reimbursement\
    WHERE org_id IN ( SELECT id FROM oa_org WHERE pid = "+org+" or id="+org+") AND is_paid = 1 AND SUBSTR(create_date, 1, 4) = "+time+"\
    GROUP BY SUBSTR(create_date, 1, 7)) a ON b.`month` = create_date ORDER BY b.`month`"
    data=db.session.execute(sql).fetchall()
    column_text=[u'金额(元)']
    obj = OA_Org.query.filter_by(id=org).first()
    return exp.bar_3d(data,u"",column_text,obj.name,time)
	
# 统计报表-月度部门费用开支情况搜索
@app.route('/tjbb/ydbmtj_search', methods=['GET'])
def ydbmtj_search():
    org = OA_Org.query.filter_by(manager=current_user.id).first()
    data = ''
    if org:
        data = get_recursion_org(org.id)
    if str(current_user.id) == '1':
        data = OA_Org.query.all()
    return render_template("tjbb/ydbmtj_search.html",data=data)
	
# 统计报表-月度部门费用开支情况
@app.route('/tjbb/ydbmtj', methods=['POST'])
def ydbmtj():
    org = request.form['org']
    time = request.form['time']
    return render_template("tjbb/ydbmtj.html",org=org,time=time)	

# 部门月开支饼状图
@app.route('/Report/create/pie/<org>/<time>', methods=['GET'])
def Report_create_pie(org,time):
    exp = flash_pic()
    sql ="select b.reason_name as name,sum(a.amount) as amount from oa_reimbursement a,oa_reason b where a.org_id="+org+" \
    and a.reason=b.id and is_paid=1 and date_format(a.create_date,'%Y-%m')='"+time+"' GROUP BY a.reason"
    data=db.session.execute(sql).fetchall()
    obj = OA_Org.query.filter_by(id=org).first()
    title = obj.name+"部门"+time+"月费用开支"
    return exp.pie(data,title)

	
# 统计报表-月度公司费用开支情况搜索
@app.route('/tjbb/ydgstj_search', methods=['GET'])
def ydgstj_search():
    data=''
    if str(current_user.id) == '1':
        data = OA_Org.query.all()
    else:
        data = OA_Org.query.filter_by(manager=current_user.id).all()
        if data[0].org_level==0:
            data = OA_Org.query.filter("pid=1").all()
    return render_template("tjbb/ydgstj_search.html",data=data)
	
# 统计报表-月度公司费用开支情况
@app.route('/tjbb/ydgstj', methods=['POST'])
def ydgstj():
    org = request.form['org']
    time = request.form['time']
    return render_template("tjbb/ydgstj.html",org=org,time=time)

# 公司月开支饼状图
@app.route('/Report/create/pieOrg/<org>/<time>', methods=['GET'])
def Report_create_pieOrg(org,time):
    exp = flash_pic()
    sql ="select b.reason_name,sum(a.amount) from oa_reimbursement a,oa_reason b where \
    a.org_id in (select id from oa_org where id="+org+" or pid="+org+")\
    and a.reason=b.id and is_paid=1 and date_format(a.create_date,'%Y-%m')='"+time+"' GROUP BY a.reason"
    data=db.session.execute(sql).fetchall()
    obj = OA_Org.query.filter_by(id=org).first()
    title = obj.name+"公司"+time+"月费用开支"
    return exp.pie(data,title)
	
# 统计报表-季度部门费用开支情况搜索
@app.route('/tjbb/jdbmtj_search', methods=['GET'])
def jdbmtj_search():
    org = OA_Org.query.filter_by(manager=current_user.id).first()
    data = ''
    if org:
        data = get_recursion_org(org.id)
    if str(current_user.id) == '1':
        data = OA_Org.query.all()
    return render_template("tjbb/jdbmtj_search.html",data=data)
	
# 统计报表-季度部门费用开支情况
@app.route('/tjbb/jdbmtj', methods=['POST'])
def jdbmtj():
    org = request.form['org']
    year = request.form['year']
    quarter = request.form['quarter']
    return render_template("tjbb/jdbmtj.html",org=org,year=year,quarter=quarter)

# 部门季度开支饼状图
@app.route('/Report/create/pieQuarter/<org>/<year>/<quarter>', methods=['GET'])
def Report_create_pieQuarter(org,year,quarter):
    exp = flash_pic()
    time = ""
    string = ""
    if quarter=='1':
        time+="('"+year+"-01','"+year+"-02','"+year+"-03')"
        string="第一季度"
    if quarter=='2':
        time+="('"+year+"-04','"+year+"-05','"+year+"-06')"
        string="第二季度"
    if quarter=='3':
        time+="('"+year+"-07','"+year+"-08','"+year+"-09')"
        string="第三季度"
    if quarter=='4':
        time+="('"+year+"-10','"+year+"-11','"+year+"-12')"
        string="第四季度"
    sql ="select b.reason_name,sum(a.amount) from oa_reimbursement a,oa_reason b where a.org_id="+org+" \
    and a.reason=b.id and is_paid=1 and date_format(a.create_date,'%Y-%m') in "+time+" GROUP BY a.reason"
    data=db.session.execute(sql).fetchall()
    obj = OA_Org.query.filter_by(id=org).first()
    title = obj.name+"部门"+year+string+"费用开支"
    return exp.pie(data,title)	
	
# 统计报表-季度公司费用开支情况搜索
@app.route('/tjbb/jdgstj_search', methods=['GET'])
def jdgstj_search():
    data=''
    if str(current_user.id) == '1':
        data = OA_Org.query.all()
    else:
        data = OA_Org.query.filter_by(manager=current_user.id).all()
        if data[0].org_level==0:
            data = OA_Org.query.filter("pid=1").all()
    return render_template("tjbb/jdgstj_search.html",data=data)
	
# 统计报表-季度公司费用开支情况
@app.route('/tjbb/jdgstj', methods=['POST'])
def jdgstj():
    org = request.form['org']
    year = request.form['year']
    quarter = request.form['quarter']
    return render_template("tjbb/jdgstj.html",org=org,year=year,quarter=quarter)

# 公司季度开支饼状图
@app.route('/Report/create/pieOrgQuarter/<org>/<year>/<quarter>', methods=['GET'])
def Report_create_pieOrgQuarter(org,year,quarter):
    exp = flash_pic()
    time = ""
    string = ""
    if quarter=='1':
        time+="('"+year+"-01','"+year+"-02','"+year+"-03')"
        string="第一季度"
    if quarter=='2':
        time+="('"+year+"-04','"+year+"-05','"+year+"-06')"
        string="第二季度"
    if quarter=='3':
        time+="('"+year+"-07','"+year+"-08','"+year+"-09')"
        string="第三季度"
    if quarter=='4':
        time+="('"+year+"-10','"+year+"-11','"+year+"-12')"
        string="第四季度"
    sql ="select b.reason_name,sum(a.amount) from oa_reimbursement a,oa_reason b where \
    a.org_id in (select id from oa_org where id="+org+" or pid="+org+") \
    and a.reason=b.id and is_paid=1 and date_format(a.create_date,'%Y-%m') in "+time+" GROUP BY a.reason"
    data=db.session.execute(sql).fetchall()
    obj = OA_Org.query.filter_by(id=org).first()
    title = obj.name+"公司"+year+string+"费用开支"
    return exp.pie(data,title)  

#递归获取所有部门
def get_recursion_org(pid):
    tmpsql = "FIND_IN_SET(id,getChildOrgLst('"+str(pid)+"'))"
    orgs_list = OA_Org.query.filter(tmpsql).all()
    return orgs_list

#递归获取所管部门和项目
def get_recursion_project(user_id):
    sql = ''
    ids = []
    org_ids = "("
    project_ids = "("
    org = OA_Org.query.filter_by(manager=user_id).all()
    if len(org)>0:#选定部门，递归查询子部门及子项目
        for node_obj in org: 
            tmpsql = "FIND_IN_SET(id ,getChildOrgLst('"+str(node_obj.id)+"'))"
            orgs_list = OA_Org.query.filter(tmpsql).all()
            orgs_list = list(set(orgs_list))
            projects_list = []
            
            for obj in orgs_list:
                projects = OA_Project.query.filter_by(p_org_id=obj.id).all()
                org_ids+=str(obj.id)+","

                if projects:
                    for obj2 in projects:
                        tmpsql = "FIND_IN_SET(id ,getChildProjectLst('"+str(obj2.id)+"'))"
                        projects_list += OA_Project.query.filter(tmpsql).all()
            
            projects_list = list(set(projects_list))
            if projects_list:
                for obj in projects_list:
                    ids.append(obj.id)
                    project_ids+=str(obj.id)+","  
    project = OA_Project.query.filter_by(manager_id=current_user.id).all()
    if len(project)>0:#选定项目，递归查询子项目
        for node_obj in project: 
            tmpsql = "FIND_IN_SET(id ,getChildProjectLst('"+str(node_obj.id)+"'))"
            projects_list = OA_Project.query.filter(tmpsql).all()
            projects_list = list(set(projects_list))
            
            if projects_list:
                for obj in projects_list:
                    project_ids+=str(obj.id)+"," 

    org_ids = str(org_ids[0:len(org_ids)-1])+")"       
    project_ids = str(project_ids[0:len(project_ids)-1])+")"
    #获取部门和项目的所有成员
    sql = "select DISTINCT user_id from oa_project_group where (type='OA_Org' and project_id in "+org_ids+") "
    if len(ids)>0:
        sql+="or (type='OA_Project' and project_id in "+project_ids+")"   

    #获取项目管理中项目id
    task_sql = "select * from oa_task_main where create_user in ("+sql+") group by id"
    data = db.session.execute(task_sql).fetchall()
    return data

#递归获取所管部门下的所有项目内容
def get_recursion_project_task(org_id,task_name):
    sql = ''
    ids = []
    org_ids = "("
    project_ids = "("
    org = OA_Org.query.filter_by(id=org_id).first()
    if org:#选定部门，递归查询子部门及子项目
        tmpsql = "FIND_IN_SET(id ,getChildOrgLst('"+str(org.id)+"'))"
        orgs_list = OA_Org.query.filter(tmpsql).all()
        orgs_list = list(set(orgs_list))
        projects_list = []
        
        for obj in orgs_list:
            projects = OA_Project.query.filter_by(p_org_id=obj.id).all()
            org_ids+=str(obj.id)+","

            if projects:
                for obj2 in projects:
                    tmpsql = "FIND_IN_SET(id ,getChildProjectLst('"+str(obj2.id)+"'))"
                    projects_list += OA_Project.query.filter(tmpsql).all()
        
        projects_list = list(set(projects_list))
        if projects_list:
            for obj in projects_list:
                ids.append(obj.id)
                project_ids+=str(obj.id)+","  
    org_ids = str(org_ids[0:len(org_ids)-1])+")"       
    project_ids = str(project_ids[0:len(project_ids)-1])+")"
    #获取部门和项目的所有成员
    sql = "select DISTINCT user_id from oa_project_group where (type='OA_Org' and project_id in "+org_ids+") "
    if len(ids)>0:
        sql+="or (type='OA_Project' and project_id in "+project_ids+")"   

    #获取项目管理中项目id
    task_sql = "select * from oa_task_main where create_user in ("+sql+")"
    if str(task_name) != "-1":
        task_sql += " and subject like '%"+task_name+"%'"
    task_sql += " group by id"
    print task_sql
    data = db.session.execute(task_sql).fetchall()
    return data