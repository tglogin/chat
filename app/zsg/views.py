from . import zsg


# 示例
# 本地测试访问地址 http://localhost:5000/sendMsg
@zsg.route('/sendMsg')
def add_fri():
    return '发送消息成功'
