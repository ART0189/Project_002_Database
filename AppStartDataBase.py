from flask import Flask
#from flask_script import Manager,Server
import DataBaseConfig
from DataBase import db
from Constructor.ConstructHelper import ConstructTest
import Interface.Player.PlayerBaseInfoModify as PBIM
import Interface.Player.PlayerModify_002 as PM_002
import Interface.Player.PlayerModify_004 as PM_004

from TestRequests.TestDBReqHelper import *

#init
#Init application from DataBaseConfig by flask
DataBaseApp = Flask(__name__)
DataBaseApp.config.from_object(DataBaseConfig)
db.init_app(DataBaseApp)
#DataBaseManager=Manager(DataBaseApp)
#DataBaseManager.add_command("runserver", Server(host='0.0.0.0', port=5000, use_debugger=True, use_reloader=True))

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

    #RegisterBaseRequest('RegTest','XXXX',183023)
    #Register002Request('RegTest002',3,'NoHardware')
    #Login002Request('Ayanami','UnInitedHardwareCode')

    return "hello"

#launch
#launch databse local debug
if __name__ == '__main__':
    #LocalDataBase

    print('Main DataBase Start!')
    print('Project002 DataBase Start!')
    print('Project004 DataBase Start!')
    DataBaseApp.run(debug=True)
