#coding:utf-8
import os

# 引入日志模块
import logging
import logging.config

_HERE = os.path.dirname(__file__)
_DB_SQLITE_PATH = os.path.join(_HERE, 'scapp.sqlite')

# ========配置日志开始=================
_LOG_PATH=os.path.join(_HERE, 'log')
if not os.path.exists(_LOG_PATH):
    os.mkdir(_LOG_PATH)
_LOG_FILE_PATH=os.path.join(_LOG_PATH,'scapp.log')
logger = logging.getLogger('scapp')
hdlr = logging.FileHandler(_LOG_FILE_PATH)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.WARNING)
#====================================

_DBUSER = "root"  # 数据库用户名
_DBPASS = "root"  # 数据库用户名密码
_DBHOST = "192.168.0.250"  # 服务器
_DBPORT = '3306' #服务器端口
_DBNAME = "new_oa"  # 数据库名称

PER_PAGE = 10  # 每页数量

class Config(object):
    SECRET_KEY = '\xb5\xc8\xfb\x18\xba\xc7*\x03\xbe\x91{\xfd\xe0L\x9f\xe3\\\xb3\xb1P\xac\xab\x061'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % _DB_SQLITE_PATH
    BABEL_DEFAULT_TIMEZONE = 'Asia/Chongqing'

# 当前用的数据库配置 重写"SQLALCHEMY_DATABASE_URI"为mysql
class ProConfig(Config):
    # 微贷系统数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (_DBUSER, _DBPASS, _DBHOST, _DBPORT, _DBNAME)
    #SQLALCHEMY_DATABASE_URI = 'ibm_db_sa://%s:%s@%s:%s/%s' % (_DBUSER, _DBPASS, _DBHOST, _DBPORT, _DBNAME)
    DEBUG = True

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    TESTING = True