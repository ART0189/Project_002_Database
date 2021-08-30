from flask import Flask
import DataBaseConfig as DataBaseConfig
from DataBase import db

#init
#Init application from DataBaseConfig by flask
app = Flask(__name__)
app.config.from_object(DataBaseConfig)
db.init_app(app)

#register
#register on json by blueprint, use url_prefix to define the type that called by url
#they are uesd in interfaces which contains functions without the prefix 'Py', and just for test and frontend call

#app.register_blueprint(um.user,url_prefix="/user")
#app.register_blueprint(rm.restaurant,url_prefix="/restaurant")
#app.register_blueprint(dm.dish,url_prefix="/dish")
#app.register_blueprint(om.order,url_prefix='/order')


#start
#called when open localhost if database use localhost as uri config
#do database base construct or other database init operations
#can remove if use database manager or .sql
@app.route('/')
def Start():
    '''
    db.drop_all()
    db.create_all()
    DataBaseConstruct_ALL(1)
    '''

    #om.PyFind_OrderTime(datetime.date.today())
    #GenericModify(1,1,'User','Telephone',123456)
    #GenericModify(2, 15, 'User')
    #GenericModify(3,1,'User',['Gender','Address'],['\'男\'','\'下北泽\''])

    #Tp_DishList=dm.PyList()
    #print(Tp_DishList)

    return "hello"

#launch
#launch databse local debug
if __name__ == '__main__':
    #LocalDataBase

    app.run(debug=True)
