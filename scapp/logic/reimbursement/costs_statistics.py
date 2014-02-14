# coding:utf-8
__author__ = 'johhny'

from scapp import db


def get_total_apply_costs(org_id):
    if org_id != -1:
        str_query_string="SELECT SUM(amount) AS t_amount FROM oa_reimbursement WHERE org_id=%s"%(org_id)
    else:
        str_query_string="SELECT SUM(amount) AS t_amount FROM oa_reimbursement"

    result=db.session.execute(str_query_string).fetchall()
    for data in result:
        total_amount=data['t_amount']
    return total_amount if total_amount is not None else 0


def get_total_paid_costs(org_id):
    if org_id != -1:
        str_query_string="SELECT SUM(amount) AS t_amount FROM oa_reimbursement WHERE is_paid='1' AND org_id=%s"%(org_id)
    else:
        str_query_string="SELECT SUM(amount) AS t_amount FROM oa_reimbursement WHERE is_paid='1'"
    
    result=db.session.execute(str_query_string).fetchall()
    for data in result:
        total_amount=data['t_amount']
    return total_amount if total_amount is not None else 0


def get_monthly_paid_costs(org_id):
    if org_id != -1:
        str_query_string="SELECT SUM(amount) AS t_amount FROM oa_reimbursement " \
                     "WHERE is_paid='1' AND month(paid_date) =month(curdate()) " \
                     "AND year(paid_date) = year(curdate()) AND org_id=%s"%(org_id)
    else:
        str_query_string="SELECT SUM(amount) AS t_amount FROM oa_reimbursement " \
                     "WHERE is_paid='1' AND month(paid_date) =month(curdate()) " \
                     "AND year(paid_date) = year(curdate())"

    result=db.session.execute(str_query_string).fetchall()
    for data in result:
        total_amount=data['t_amount']
    return total_amount if total_amount is not None else 0


def get_season_paid_costs(org_id):
    if org_id != -1:
        str_query_string="SELECT SUM(amount) AS t_amount FROM oa_reimbursement " \
                     "WHERE is_paid='1' AND quarter( FROM_UNIXTIME( paid_date ) ) = quarter( curdate( )) " \
                     " AND org_id=%s"%(org_id)
    else:
        str_query_string="SELECT SUM(amount) AS t_amount FROM oa_reimbursement " \
                     "WHERE is_paid='1' AND quarter( FROM_UNIXTIME( paid_date ) ) = quarter( curdate( )) "

    result=db.session.execute(str_query_string).fetchall()
    for data in result:
        total_amount=data['t_amount']
    return total_amount if total_amount is not None else 0