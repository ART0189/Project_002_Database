from flask import Flask
import DataBaseConfig
from DataBase import db
from Constructor.ConstructHelper import ConstructTest
import Interface.Player.PlayerBaseInfoModify as PBIM
import Interface.Player.PlayerModify_002 as PM_002
import  Interface.Player.PlayerModify_004 as PM_004

#init
#Init application from DataBaseConfig by flask
DataBaseApp = Flask(__name__)
DataBaseApp.config.from_object(DataBaseConfig)
db.init_app(DataBaseApp)

#register
#register on json by blueprint, use url_prefix to define the type that called by url
#they are uesd in interfaces which contains + without the prefix 'Py', and just for test and frontend call

DataBaseApp.register_blueprint(PBIM.baseinfomodify,url_prefix="/baseinfomodify")
DataBaseApp.register_blueprint(PM_002.playermodify_002,url_prefix="/playermodify002")
DataBaseApp.register_blueprint(PM_004.playermodify_004,url_prefix="/playermodify004")
#app.register_blueprint(dm.dish,url_prefix="/dish")
#app.register_blueprint(om.order,url_prefix='/order')


#start
#called when open localhost if database use localhost as uri config
#do database base construct or other database init operations
#can remove if use database manager or .sql
@DataBaseApp.route('/')
def Start():
    '''
    db.drop_all()
    db.create_all()
    ConstructTest()
    '''

    return "hello"

#launch
#launch databse local debug
if __name__ == '__main__':
    #LocalDataBase

    print('Main DataBase Start!')
    print('Project002 DataBase Start!')
    print('Project004 DataBase Start!')
    DataBaseApp.run(debug=True)
