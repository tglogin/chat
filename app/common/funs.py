from flask import request, session

# 判断用户是否登录
def chkLogin():
    user_no = request.args.get('user_no', 0)
    if not user_no:
        user_no = request.cookies.get('user_no')
    # 看服务器session中是否存在该用户
    res = session.get(str(user_no))
    if res:
        return user_no
