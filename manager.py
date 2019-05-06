# 管理和启动项目
from app import create_app

app = create_app()

# app.config['SQLALCHEMY_ECHO']=True
if __name__ == '__main__':
    app.run(host='0.0.0.0')
