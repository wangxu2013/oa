# coding:utf-8
from scapp import db
from scapp.config import PER_PAGE
from scapp.config import logger
from scapp.config import Approval_type_ORG,Approval_type_PRJ,Approval_type_CAIWU
import scapp.helpers as helpers
import datetime,time
import json

from flask import Module, session, request, render_template, redirect, url_for, flash
from flask.ext.login import current_user

from scapp.models import OA_Project,OA_Reason,OA_Org,OA_User,OA_UserRole,OA_Reimbursement
from scapp.logic import recursion

from scapp import app

from scapp.tools.export_excel import export_excel
import xlwt,re
ezxf=xlwt.easyxf #样式转换

#费用统计条件树
@app.route('/fytj/fytj_tree',methods=['GET','POST'])
def fytj_tree():
    user = '';
    #财务能看到所有报销
    if str(current_user.id) =='49':
        user = '25'
    else:
        user = current_user.id
    orgs = OA_Org.query.filter("manager="+str(user)+" and version='2015'").all()
    orgs_list = []
    if orgs:
        for obj in orgs:
            sql = "FIND_IN_SET(id ,getChildOrgLst('"+str(obj.id)+"'))"
            orgs_list += OA_Org.query.filter(sql).all()
    
    orgs_json = helpers.show_result_content(list(set(orgs_list)))
    orgs_json_obj = json.loads(orgs_json)
    
    for json_obj in orgs_json_obj:
        json_obj['type'] = "OA_Org"
        json_obj['icon'] = "/static/css/zTreeStyle/img/diy/1_open.png"
        projects = OA_Project.query.filter_by(p_org_id=json_obj["id"]).all()
        if projects:
            for pro_obj in projects:
                sql = "FIND_IN_SET(id ,getChildProjectLst('"+str(pro_obj.id)+"'))"
                projects_list = OA_Project.query.filter(sql).all()
                for objP in projects_list:
                    objP.name = objP.project_name
                    objP.type = "OA_Project"
                    objP.icon = "/static/css/zTreeStyle/img/diy/2.png"
                    
            json_obj['children'] = json.loads(helpers.show_result_content(projects))
        
    return json.dumps(orgs_json_obj)# 返回json

#费用统计
@app.route('/fytj/fytj_search',methods=['GET'])
def fytj_search():
    return render_template("bxsq/fytj/fytj_search.html")

#费用统计
@app.route('/fytj/fytj_list/<int:page>',methods=['GET','POST'])
def fytj_list(page):
    if request.method == 'POST':
        beg_date = request.form['beg_date'] + " 00:00:00"
        end_date = request.form['end_date'] + " 23:59:59"
        is_paid = request.form['is_paid']
        node_id = request.form['node_id']
        node_type = request.form['node_type']
        
        sql = "1=1"
        if is_paid != '-1':
            sql += " and is_paid = "+is_paid
        sql += " and create_date between '" + beg_date + "' and '" + end_date + "'"
        
        sql += " and project_id in ("
        ids = recursion.get_recursion_prjs(node_id, node_type)
        for obj in ids:
            sql += str(obj) + ","
        sql += "-1)"
        
        data=OA_Reimbursement.query.filter(sql).order_by("id").paginate(page, per_page = PER_PAGE)
        
        return render_template("bxsq/fytj/fytj_list.html",data=data,beg_date=beg_date,end_date=end_date,is_paid=is_paid,node_id=node_id,node_type=node_type)

#费用支付Excel下载
@app.route('/fytj/fytj_Excel',methods=['GET','POST'])
def fytj_Excel():
    beg_date = request.form['beg_date'] + " 00:00:00"
    end_date = request.form['end_date'] + " 23:59:59"
    is_paid = request.form['is_paid']
    node_id = request.form['node_id']
    node_type = request.form['node_type']
    sql = "SELECT b.name,c.real_name,d.project_name,a.amount,a.`describe`,a.create_date,(case is_paid when '0' then '未支付' \
        when '1' then '已支付' end) as paid,a.paid_date FROM oa_reimbursement a, oa_org b, oa_user c,oa_project d WHERE\
        a.org_id = b.id AND a.create_user = c.id and a.project_id=d.id"
    if is_paid != '-1':
        sql += " and a.is_paid = "+is_paid
    sql += " and a.create_date between '" + beg_date + "' and '" + end_date + "'"
    
    sql += " and a.project_id in ("
    ids = recursion.get_recursion_prjs(node_id, node_type)
    for obj in ids:
        sql += str(obj) + ","
    sql += "-1)"
    data=db.session.execute(sql).fetchall()

    exl_hdngs=['费用所属单位','申请人','项目','金额','报销事由','创建时间','审批状态','支付时间']
    types=     'text   text   text      text      text     datetime    text   datetime'.split()
    exl_hdngs_xf=ezxf('font: bold on;align: wrap on,vert centre,horiz center')
    types_to_xf_map={
        'int':ezxf(num_format_str='#,##0'),
        'date':ezxf(num_format_str='yyyy-mm-dd'),
        'datetime':ezxf(num_format_str='yyyy-mm-dd HH:MM:SS'),
        'ratio':ezxf(num_format_str='#,##0.00%'),
        'text':ezxf(),
        'price':ezxf(num_format_str='￥#,##0.00')
    }

    data_xfs=[types_to_xf_map[t] for t in types]
    date=datetime.datetime.now()
    year=date.year
    month=date.month
    day=date.day
    filename=str(year)+'_'+str(month)+'_'+str(day)+'_'+'报销费用支付详情'+'.xls'
    exp=export_excel()
    return exp.export_download(filename,'报销费用支付详情表',exl_hdngs,data,exl_hdngs_xf,data_xfs)