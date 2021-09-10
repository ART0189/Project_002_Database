from DataBase import db
from flask import Blueprint, jsonify, request
from Models.Player.Player_002 import Player_002

playermodify_002 = Blueprint('playermodify002', __name__)

def PyUnsafeAddPlayer_002(playername,hardwarecode):
    '''
    You shouldn't use it! Add any player of any project in player base info modify
    :param playername: player name
    :return: player_002 obj
    '''
    player_002 = Player_002(PlayerName=playername, HardwareCode=hardwarecode)
    db.session.add(player_002)
    db.session.commit()
    return player_002

@playermodify_002.route('/login',methods=['GET','POST'])
def Login_002_Api():
    DataBaseResponse={'code':1,'message':'Find Failed','data':{"ErrorMessage":"ErrorMessage"}}
    ClientRequest=request.values
    if 'BaseID' in ClientRequest:
        BaseID=ClientRequest['BaseID']
    else:
        return jsonify(DataBaseResponse)
    if 'PlayerName' in ClientRequest:
        PlayerName=ClientRequest['PlayerName']
    else:
        return jsonify(DataBaseResponse)
    if 'HardwareCode' in ClientRequest:
        PlayerHardwareCode=ClientRequest['HardwareCode']
    else:
        return jsonify(DataBaseResponse)
    PlayerInfo=PyFind_Name_002(PlayerName)
    if PlayerInfo:
        if(PlayerInfo.HardwareCode==PlayerHardwareCode):
            DataBaseResponse['code']=200
            DataBaseResponse['message']='Find Success'

    return jsonify(DataBaseResponse)

def PyFind_ID_002(playerid):
    return Player_002.query.get(playerid)

def PyFind_Name_002(playername):
    return Player_002.query.filter_by(PlayerName=playername).first()

def PyCheckPlayer_002(playername,hardwarecode):
    return PyFind_Name_002(playername).HardwareCode==hardwarecode