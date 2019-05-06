from app.common.funs import chkLogin
from . import tg
from flask import render_template, request, session, redirect, make_response
from .models import *
import json
import hashlib


@tg.route('/')
@tg.route('/index')
def main_index():
    # 判断用户是否已经登录，并获取用户的易号
    user_no = chkLogin()
    if user_no:
        return render_template('index.html')
    return redirect('/login')


@tg.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        user_no = chkLogin()
        if user_no:
            return redirect('/index?user_no=' + str(user_no))
        return render_template('login.html')
    else:
        user_name = request.form['user_name']
        user_pwd = request.form['user_pwd']
        reme = request.form.get('chkRememberMe', 0)
        # 查询数据库,判断用户名或密码是否正确
        res = chkUserPwd(user_name, user_pwd)
        if res:
            data = {
                'status': 1,
                'msg': '登录成功',
                'data': {'usre_id': res.user_id, 'user_no': res.user_no, 'user_name': user_name}
            }
            session[str(res.user_no)] = {'user_name': user_name, 'user_pwd': user_pwd}

            resp = make_response(json.dumps(data))
            resp.set_cookie('user_no', str(res.user_no), 60 * 30)
            return resp
        else:
            data = {
                'status': 0,
                'msg': '用户名或密码错误',
                'data': []
            }
        return json.dumps(data)
