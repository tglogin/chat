"""
# 对整个的应用做初始化的操作
# 主要工作
    1.构建Flask应用以及各种配置
    2.构建SQLAlchemy的应用

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from app.common.db_config import *

pymysql.install_as_MySQLdb()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # 配置启动模式
    app.config['DEBUG'] = True  # 调试模式
    # 配置数据库的连接字符串
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{}:{}@{}:{}/{}".format(USER_NAME, USER_PWD, HOST, PORT,
                                                                            DATABASE_NAME)
     # 取消信号追踪
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 配置自动提交
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    # 配置SECRET_KEY,SESSION时使用
    app.config['SECRET_KEY'] = 'yiliao'
    # 数据库应用实例的初始化
    db.init_app(app)

    # 将main蓝图程序关联到app上
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .tg import tg as tg_blueprint
    app.register_blueprint(tg_blueprint)

    from .hhb import hhb as hhb_blueprint
    app.register_blueprint(hhb_blueprint)

    from .szh import szh as hhb_blueprint
    app.register_blueprint(hhb_blueprint)

    from .wxx import wxx as hhb_blueprint
    app.register_blueprint(hhb_blueprint)

    from .zsg import zsg as hhb_blueprint
    app.register_blueprint(hhb_blueprint)

    return app
