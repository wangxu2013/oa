# coding:utf-8
from scapp import db
from scapp.models import OA_Project,OA_Org
from flask.ext.login import current_user

'''
递归获取所有子项目id
node_id（部门id或项目id）,node_type（标示部门或项目）
'''
def get_recursion_prjs(node_id,node_type):
    ids = []
    if node_id:
        if node_type == "OA_Org":#选定部门，递归查询子部门及子项目
            tmpsql = "FIND_IN_SET(id ,getChildOrgLst('"+node_id+"'))"
            orgs_list = OA_Org.query.filter(tmpsql).all()
            orgs_list = list(set(orgs_list))
            projects_list = []
            for obj in orgs_list:
                projects = OA_Project.query.filter_by(p_org_id=obj.id).all()
                if projects:
                    for obj2 in projects:
                        tmpsql = "FIND_IN_SET(id ,getChildProjectLst('"+str(obj2.id)+"'))"
                        projects_list += OA_Project.query.filter(tmpsql).all()
            projects_list = list(set(projects_list))
            if projects_list:
                for obj in projects_list:
                    ids.append(obj.id)
        else:#选定项目，递归查询子项目
            tmpsql = "FIND_IN_SET(id ,getChildProjectLst('"+node_id+"'))"
            projects_list = OA_Project.query.filter(tmpsql).all()
            projects_list = list(set(projects_list))
            if projects_list:
                for obj in projects_list:
                    ids.append(obj.id)
    else:#未选定任意节点
        orgs = OA_Org.query.filter_by(manager=current_user.id).all()#获得负责部门
        orgs_list = []
        projects_list = []
        if orgs:
            for obj in orgs:
                tmpsql = "FIND_IN_SET(id ,getChildOrgLst('"+str(obj.id)+"'))"
                orgs_list += OA_Org.query.filter(tmpsql).all()
                orgs_list = list(set(orgs_list))
                for obj2 in orgs_list:
                    projects = OA_Project.query.filter_by(p_org_id=obj2.id).all()
                    if projects:
                        for obj3 in projects:
                            tmpsql = "FIND_IN_SET(id ,getChildProjectLst('"+str(obj3.id)+"'))"
                            projects_list += OA_Project.query.filter(tmpsql).all()
            projects_list = list(set(projects_list))
            if projects_list:
                for obj3 in projects_list:
                    ids.append(obj3.id)
    print ids
    return ids