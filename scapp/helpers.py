#coding:utf-8

import unicodedata
import re

import json
from sqlalchemy.ext.declarative import DeclarativeMeta

# json转码
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata' and x != 'query' and x != 'query_class']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data, ensure_ascii = False) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = str(data)
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

# 返回内容
def show_result_content(obj):
    return json.dumps(obj, cls=AlchemyEncoder,ensure_ascii = False) #json文本

# 返回成功提示
def show_result_success(info):
    return json.dumps({'result':'Success','info':info})

# 返回失败提示
def show_result_fail(info):
    return json.dumps({'result':'Failed','info':info})
