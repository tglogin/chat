from . import hhb


# 示例
# 本地测试访问地址 http://localhost:5000/addFri
@hhb.route('/addFri')
def add_fri():
    return '添加好友成功'
