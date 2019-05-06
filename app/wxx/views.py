from . import wxx


# 示例
# 本地测试访问地址 http://localhost:5000/delFri
@wxx.route('/delFri')
def add_fri():
    return '删除好友成功'
