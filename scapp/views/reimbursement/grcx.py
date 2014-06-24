# coding:utf-8
from scapp import db
from scapp.config import PER_PAGE
from scapp.config import logger
from scapp.config import Approval_type_ORG,Approval_type_PRJ,Approval_type_CAIWU
import scapp.helpers as helpers
import datetime

from flask import Module, session, request, render_template, redirect, url_for, flash
from flask.ext.login import current_user

from scapp.models import OA_Project,OA_Reason,OA_Org,OA_UserRole,OA_Reimbursement

from scapp import app

# 个人费用
@app.route('/grcx/grcx_search', methods=['GET','POST'])
def grcx_search():
    return render_template("bxsq/grcx/grcx_search.html")

#个人费用
@app.route('/grcx/grcx_list/<int:page>/<return_type>',methods=['GET','POST'])
def grcx_list(page,return_type):
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
            return render_template("bxsq/grcx/grcx_list.html",data=data,beg_date=request.form['beg_date'],end_date=request.form['end_date'],is_paid=request.form['is_paid'])



