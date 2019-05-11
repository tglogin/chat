from flask import request, session, json
import socket, struct, time, os


# 判断用户是否登录
def chkLogin():
    user_no = request.args.get('user_no', 0)
    if not user_no:
        user_no = request.cookies.get('user_no')
    # 看服务器session中是否存在该用户
    res = session.get(str(user_no))
    if res:
        return user_no


# 获取当前日期时间
def get_now_date():
    now_time = time.time()
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now_time))


# 获取当前时间戳（毫秒）
def get_mill_time():
    return int(time.time() * 1000)


# 获取当前时间戳（秒）
def get_time():
    return int(time.time())


# 如果不存在文件/目录，就创建
def chk_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


# 将字符串ip转为int类型ip
def ip2int(str_ip):
    if str_ip:
        return int(struct.unpack('>I', socket.inet_aton(str_ip))[0])


# 将int类型ip转为字符串ip
def ip2str(int_ip):
    if int_ip:
        return socket.inet_ntoa(struct.pack('>I', int_ip))


# 返回成功信息
def ret_sucess(msg, data={}, status=1):
    data = {
        'status': status,
        'msg': msg,
        'data': data
    }
    return json.dumps(data)


# 返回失败信息
def ret_error(msg, status=0, data={}):
    data = {
        'status': status,
        'msg': msg,
        'data': data
    }
    return json.dumps(data)
