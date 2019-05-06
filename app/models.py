# 声明所有实体类
# 导入db,以便在实体类中使用
from . import db


class User(db.Model):
    """
    用户表
    """
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    user_no = db.Column(db.Integer)
    user_type = db.Column(db.Integer, default=1)
    user_nick_name = db.Column(db.String(128))
    user_pwd = db.Column(db.String(40))
    user_tel = db.Column(db.String(11))
    user_email = db.Column(db.String(48))
    user_head_pic = db.Column(db.String(128))
    pic_name = db.Column(db.String(128))
    login_ip = db.Column(db.Integer)
    login_status = db.Column(db.Integer)
    add_time = db.Column(db.Integer)


class Ylgroup(db.Model):
    """
    群表
    """
    __tablename__ = 'yl_group'
    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(100))
    group_master_id = db.Column(db.Integer)
    num = db.Column(db.Integer, default=1)
    notice = db.Column(db.String(600))
    add_time = db.Column(db.Integer)


class GroupUser(db.Model):
    """
    群用户表
    """
    __tablename__ = 'group_user'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    group_id = db.Column(db.Integer)
    user_nick_name = db.Column(db.String(128))
    user_pic = db.Column(db.String(128))
    add_time = db.Column(db.Integer)


class GroupChatRecords(db.Model):
    """
    聊天记录
    """
    __tablename__ = 'group_chat_records'
    record_id = db.Column(db.Integer, primary_key=True)
    send_user_id = db.Column(db.Integer)
    group_id = db.Column(db.Integer)
    recv_user_id = db.Column(db.Integer)
    content = db.Column(db.LargeBinary(65535))
    content_type = db.Column(db.Integer)
    add_time = db.Column(db.Integer)


class Relation(db.Model):
    """
    关系表
    """
    __tablename__ = 'relation'
    r_id = db.Column(db.Integer, primary_key=True)
    pri_id = db.Column(db.Integer)
    sub_id = db.Column(db.Integer)
    relation_type = db.Column(db.Integer)
    add_time = db.Column(db.Integer)


class GroupFiles(db.Model):
    """
    群文件表
    """
    __tablename__ = 'group_files'
    file_id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    file_name = db.Column(db.String(200))
    file_path = db.Column(db.String(300))
    file_type = db.Column(db.Integer)
    file_size = db.Column(db.Integer)
    add_time = db.Column(db.Integer)


class UserLog(db.Model):
    """
    用户日志表
    """
    __tablename__ = 'user_log'
    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    des = db.Column(db.String(100))
    log_type = db.Column(db.Integer)
    add_time = db.Column(db.Integer)


class ErrorLog(db.Model):
    """
    错误日志表
    """
    __tablename__ = 'error_log'
    err_log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    err_des = db.Column(db.String(100))
    add_time = db.Column(db.Integer)



















