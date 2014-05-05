# coding:utf-8
__author__ = 'johhny'

from flask import render_template,request,redirect, flash
from flask.ext.login import current_user
from scapp import app,db
from scapp.config import logger,PER_PAGE
from scapp.models import OA_Org,OA_UserRole,OA_Project,OA_Reimbursement
from scapp.tools.json_encoding import DateDecimalEncoder
from scapp.logic.reimbursement import costs_statistics
import datetime
import json

#reimbursement
@app.route('/fybx/',methods=['GET'])
def get_fybx():
    return render_template("")

#add reimbursement
@app.route('/fybx/add',methods=['GET','POST'])
def add_fybx():
    if request.method=='POST':
        try:
            role = OA_UserRole.query.filter_by(user_id=current_user.id).first().role
            level = role.role_level #取得用户权限等级

            status = level;
            if level == 6:#财务总监提交的报销 置为 待财务审批(发票)
                status = 4

            if level==6:
                OA_Reimbursement(request.form['project_id'],request.form['org_id'],request.form['amount'],request.form['describe'],
                             request.form['reason'],request.form['start_date'],request.form['end_date'],
                             '0','0','','0',
                             4,status,None).add()
            else:
                OA_Reimbursement(request.form['project_id'],request.form['org_id'],request.form['amount'],request.form['describe'],
                             request.form['reason'],request.form['start_date'],request.form['end_date'],
                             '0','0','','0',
                             level,status,None).add()
            #Param:
            # project_id,amount,describe,
            # reason,is_refuse,is_paid,
            # init_level,status
            db.session.commit()
            # 消息闪现
            flash('保存成功','success')
        except:
            # 回滚
            db.session.rollback()
            logger.exception('exception')
            # 消息闪现
            flash('保存失败','error')

        return redirect('fybx/add')

    else:
        project = OA_Project.query.order_by("customer").all()

        for obj in project:
            obj.project_name=obj.customer+'-'+obj.project_name

        return render_template("bxsq/new_bxsq.html",project=project)

#edit reimbursement
@app.route('/fybx/edit/<int:id>',methods=['GET','POST'])
def edit_fybx(id):
    if request.method=='POST':
        try:
            reimbursement = OA_Reimbursement.query.filter_by(id=id).first()
            reimbursement.org_id = request.form['org_id']
            reimbursement.project_id = request.form['project_id']
            reimbursement.amount = request.form['amount']
            reimbursement.describe = request.form['describe']
            reimbursement.reason = request.form['reason']
            reimbursement.start_date = request.form['start_date']
            reimbursement.end_date = request.form['end_date']

            #编辑时充值“退回标志”
            reimbursement.is_retreat = '0'

            db.session.commit()
            # 消息闪现
            flash('保存成功','success')
        except:
            # 回滚
            db.session.rollback()
            logger.exception('exception')
            # 消息闪现
            flash('保存失败','error')

        return redirect('fybx/fksh_gr_search')

    else:
        project = OA_Project.query.order_by("id").all()
        
        for obj in project:
            obj.project_name=obj.customer+'-'+obj.project_name
            
        reimbursement = OA_Reimbursement.query.filter_by(id=id).first()
        return render_template("bxsq/edit_bxsq.html",reimbursement=reimbursement,project=project)

#query reimbursement
@app.route('/fybx/query/<int:page>/<return_type>',methods=['GET','POST'])
def get_fybx_query(page,return_type):
    if return_type:
        if return_type=='json':
            data=OA_Reimbursement.query.order_by("id").all()
            return json.dumps(data,cls=DateDecimalEncoder,ensure_ascii=False)
        else:
            beg_date = request.form['beg_date'] + " 00:00:00"
            end_date = request.form['end_date'] + " 23:59:59"
            is_paid = request.form['is_paid']

            sql = "create_date between '"+beg_date+"' and '"+end_date+"'"
            if is_paid != '-1':
                sql += " and is_paid = '"+is_paid+"'"
            sql += " and create_user = "+str(current_user.id)
            data=OA_Reimbursement.query.filter(sql).order_by("id").paginate(page, per_page = PER_PAGE)
            return render_template("bxsq/bxsq_list.html",data=data,beg_date=request.form['beg_date'],end_date=request.form['end_date'],is_paid=request.form['is_paid'])

#个人费用搜索
@app.route('/fybx/fksh_gr_search',methods=['GET'])
def fksh_gr_search():
    return render_template("bxsq/fksh_gr_search.html")

#费用审批查询
@app.route('/fybx/check_query/<int:page>/<return_type>',methods=['GET'])
def get_fybx_check_query(page,return_type):
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().role
    level = role.role_level #取得用户权限等级

    #员工只能看到自己的
    status = 1
    if level == 4 or level == 5 or level == 6:
        status = level - 1

    departmentId=current_user.department
    departmentLevel=OA_Org.query.filter_by(id=departmentId).first().org_level

    sql="org_id="+str(departmentId)
    if departmentLevel == 1:#公司
        chileDepartment=OA_Org.query.filter_by(pId=departmentId).all()
        sql="org_id in ("+str(departmentId)
        for obj in chileDepartment:
            sql+=","+str(obj.id)
        sql+=")"
    
    #财务能看到所有公司报销
    if level == 5 or level == 6:
        sql = ""
        
    if return_type:
        if return_type=='json':
            if level == 6 or level == 5:
                data=OA_Reimbursement.query.filter("is_refuse=0","is_retreat=0",sql,"status=:status","init_level<:role_level").params(status=status,role_level=level).order_by("status asc").all()
            else:
                data=OA_Reimbursement.query.filter("is_refuse=0","is_retreat=0",sql,"status<=:status","init_level<:role_level").params(status=status,role_level=level).order_by("status asc").all()
            return json.dumps(data,cls=DateDecimalEncoder,ensure_ascii=False)
        else:
            if level == 6 or level == 5:
                data=OA_Reimbursement.query.filter("is_refuse=0","is_retreat=0",sql,"status=:status","init_level<:role_level").params(status=status,role_level=level).order_by("status asc").paginate(page, per_page = PER_PAGE)
            else:
                data=OA_Reimbursement.query.filter("is_refuse=0","is_retreat=0",sql,"status<=:status","init_level<:role_level").params(status=status,role_level=level).order_by("status asc").paginate(page, per_page = PER_PAGE)
            return render_template("bxsq/check_list.html",data=data,role=role)

#费用审批
@app.route('/fybx/check/<int:id>',methods=['GET','POST'])
def check_fybx(id):
    if request.method=='POST':
        try:
            role = OA_UserRole.query.filter_by(user_id=current_user.id).first().role
            level = role.role_level #取得用户权限等级
            reimbursement = OA_Reimbursement.query.filter_by(id=id).first()


            if request.form['decision'] == '1':#通过
                if level == 6:
                    reimbursement.is_paid = '1'
                    reimbursement.paid_date= datetime.datetime.now()
                reimbursement.status = level
                reimbursement.fail_reason = ''

            if request.form['decision'] == '2':#拒绝
                reimbursement.is_refuse = '1'
                reimbursement.status = level
                reimbursement.fail_reason = request.form['fail_reason']

            if request.form['decision'] == '3':#退回
                reimbursement.is_retreat = '1'
                reimbursement.status = reimbursement.init_level
                reimbursement.fail_reason = request.form['fail_reason']

            db.session.commit()
            # 消息闪现
            flash('保存成功','success')
        except:
            # 回滚
            db.session.rollback()
            logger.exception('exception')
            # 消息闪现
            flash('保存失败','error')

        return redirect('fybx/check_query/1/pc')

    else:
        role = OA_UserRole.query.filter_by(user_id=current_user.id).first().role
        project = OA_Project.query.order_by("id").all()
        reimbursement = OA_Reimbursement.query.filter_by(id=id).first()
        return render_template("bxsq/check_bxsq.html",reimbursement=reimbursement,project=project,role=role)

# #费用统计
# @app.route('/fybx/fytj/<int:page>/<return_type>',methods=['GET'])
# def get_fytj_query(page,return_type):
#     if return_type:
#         if return_type=='json':
#             data=OA_Reimbursement.query.order_by("id").all()
#             return json.dumps(data,cls=DateDecimalEncoder,ensure_ascii=False)
#         else:
#             role = OA_UserRole.query.filter_by(user_id=current_user.id).first().role
#             level = role.role_level #取得用户权限等级
#             org_id=current_user.department
#             data=''
#             if level==4:
#                 data=query_data(page)
#                 total_apply=costs_statistics.get_total_apply_costs(org_id)
#                 total_paid=costs_statistics.get_total_paid_costs(org_id)
#                 monthly=costs_statistics.get_monthly_paid_costs(org_id)
#                 season=costs_statistics.get_season_paid_costs(org_id)
#             return render_template("bxsq/fytj.html",data=data,
#                                    total_apply=total_apply,total_paid=total_paid,
#                                    monthly=monthly,season=season)

def query_data(page,beg_date,end_date,is_paid):
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().role
    level = role.role_level #取得用户权限等级
    #员工只能看到自己的
    status = 1
    if level == 4 or level == 5 or level == 6:
        status = level - 1

    departmentId=current_user.department
    departmentLevel=OA_Org.query.filter_by(id=departmentId).first().org_level

    sql="org_id="+str(departmentId)
    if departmentLevel == 1:#公司
        chileDepartment=OA_Org.query.filter_by(pId=departmentId).all()
        sql="org_id in ("+str(departmentId)
        for obj in chileDepartment:
            sql+=","+str(obj.id)
        sql+=")"

    #财务能看到所有公司报销
    if level == 5 or level == 6:
        sql = ""
    sql += " and create_date between '"+beg_date+"' and '"+end_date+"'"
    if is_paid != '-1':
        sql += " and is_paid = '"+is_paid+"'"
    data=OA_Reimbursement.query.filter(sql).order_by("is_paid desc").paginate(page, per_page = PER_PAGE)

    return data

#付款审核搜索
@app.route('/fybx/fksh_search',methods=['GET'])
def fksh_search():
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().role
    level = role.role_level #取得用户权限等级
    return render_template("bxsq/fksh_search.html",level=level)

#付款审核
@app.route('/fybx/fksh/<int:page>/<return_type>',methods=['GET','POST'])
def get_fksh_query(page,return_type):
    role = OA_UserRole.query.filter_by(user_id=current_user.id).first().role
    level = role.role_level #取得用户权限等级
    if return_type:
        if return_type=='json':
            data=OA_Reimbursement.query.order_by("id").all()
            return json.dumps(data,cls=DateDecimalEncoder,ensure_ascii=False)
        else:
            beg_date = request.form['beg_date'] + " 00:00:00"
            end_date = request.form['end_date'] + " 23:59:59"
            is_paid = request.form['is_paid']
            if level!=4:
                org_id = request.form['org_id']
                sql = "create_date between '"+beg_date+"' and '"+end_date+"'"
                if org_id != '-1':
                    sql += " and org_id = "+org_id
                if is_paid != '-1':
                    sql += " and is_paid = '"+is_paid+"'"

                data=OA_Reimbursement.query.filter(sql).order_by("is_paid asc").paginate(page, per_page = PER_PAGE)

                total_apply=costs_statistics.get_total_apply_costs(int(org_id))
                total_paid=costs_statistics.get_total_paid_costs(int(org_id))
                monthly=costs_statistics.get_monthly_paid_costs(int(org_id))
                season=costs_statistics.get_season_paid_costs(int(org_id))

                return render_template("bxsq/fksh.html",role=role,data=data,
                                       total_apply=total_apply,total_paid=total_paid,
                                       monthly=monthly,season=season,
                                       beg_date=request.form['beg_date'],end_date=request.form['end_date'],
                                       org_id=org_id,is_paid=is_paid)

            else:
                org_id=current_user.department
                data=''
                data=query_data(page,beg_date,end_date,is_paid)
                total_apply=costs_statistics.get_total_apply_costs(org_id)
                total_paid=costs_statistics.get_total_paid_costs(org_id)
                monthly=costs_statistics.get_monthly_paid_costs(org_id)
                season=costs_statistics.get_season_paid_costs(org_id)
                return render_template("bxsq/fytj.html",data=data,
                                       total_apply=total_apply,total_paid=total_paid,
                                       monthly=monthly,season=season,beg_date=request.form['beg_date'],end_date=request.form['end_date'],
                                       is_paid=is_paid)
