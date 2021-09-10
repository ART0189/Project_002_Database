from DataBase import db
from flask import Blueprint, jsonify, request
from Models.Player.Player_002 import Player_002
from Interface.Player.PlayerBaseInfoModify import *

playermodify_002 = Blueprint('playermodify002', __name__)

def PyUnsafeAddPlayer_002(playername):
    '''
    You shouldn't use it! Add any player of any project in player base info modify
    :param playername: player name
    :return: player_002 obj
    '''
    player_002 = Player_002(PlayerName=playername)
    db.session.add(player_002)
    db.session.commit()
    return player_002

@playermodify_002.route('/login',methods=['GET','POST'])
def Login_002_Api():
    DataBaseResponse={'code':1,'ErrorMessage':'Find Failed'}
    ClientRequest=request.get_json()
    if 'BaseID' in ClientRequest:
        BaseID=ClientRequest['BaseID']
    else:
        return jsonify(DataBaseResponse)
    if 'HardwareCode' in ClientRequest:
        PlayerHardwareCode=ClientRequest['HardwareCode']
    else:
        return jsonify(DataBaseResponse)

    tpbaseinfo=PyGetBaseAccount_ID(BaseID)
    if(tpbaseinfo):
        PlayerInfo=PyGet002_ID(tpbaseinfo.Account_002)
        if(PlayerInfo):
            if(not PlayerInfo.BanStatus):
                if(PlayerInfo.HardwareCode==PlayerHardwareCode):
                    DataBaseResponse['code']=200
                    DataBaseResponse['ErrorMessage']='Find Success'
                else:
                    DataBaseResponse['ErrorMessage']='New Computer! Do additional verification please!'
            else:
                DataBaseResponse['ErrorMessage']='The Account has been banned!'
        else:
            DataBaseResponse['ErrorMessage']='The BaseAccount havent any Account002'
    else:
        DataBaseResponse['ErrorMessage']='Invalid BaseAccount!'

    return jsonify(DataBaseResponse)

def PyGet002_ID(playerid):
    return Player_002.query.get(playerid)

def PyFind_Name_002(playername):
    return Player_002.query.filter_by(PlayerName=playername).first()