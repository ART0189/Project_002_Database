from DataBase import db
from flask import Blueprint, jsonify, request
from Models.Player.PlayerBaseInfo import PlayerBase
from Interface.Player.PlayerModify_002 import *
from Interface.Player.PlayerModify_004 import *
from Interface.Ban.BanModify import *

baseinfomodify = Blueprint('baseinfomodify', __name__)


@baseinfomodify.route('/register/base',methods=['GET','POST'])
def AddPlayerBase():
    DataBaseResponse = {'code': 1, 'ErrorMessage': 'Register Failed'}
    ClientRequest = request.get_json()
    if 'BaseName' in ClientRequest:
        PlayerName = ClientRequest['BaseName']
    else:
        return jsonify(DataBaseResponse)
    if 'Password' in ClientRequest:
        PlayerPassword = ClientRequest['Password']
    else:
        return jsonify(DataBaseResponse)
    if 'Telephone' in ClientRequest:
        PlayereTelephone = ClientRequest['Telephone']
    else:
        return jsonify(DataBaseResponse)
    if 'HardwareCode' in ClientRequest:
        HardwareCode = ClientRequest['HardwareCode']
    else:
        return jsonify(DataBaseResponse)

    if(not bool(PyFind_Name_Base(PlayerName).first())):
        if(not FindTelephoneBanned(PlayereTelephone)):
            if(not FindHardwareCodeBanned(HardwareCode)):
                PlayerBaseInfo=PyAddPlayerBase(PlayerName,PlayerPassword,PlayereTelephone,HardwareCode)
                DataBaseResponse={'code': 200, 'ErrorMessage': 'Register Success', 'data': {'BaseID':PlayerBaseInfo.PlayerBaseID}}
            else:
                DataBaseResponse['ErrorMessage']='The computer has been banned!'
        else:
            DataBaseResponse['ErrorMessage']='The telephone has been banned!'
    else:
        DataBaseResponse['ErrorMessage']='Ununique BaseName'

    return jsonify(DataBaseResponse)


def PyAddPlayerBase(basename, pwd, tele, hardwarecode):
    playerbaseinfo = PlayerBase(PlayerBaseName=basename,Telephone=tele,HardwareCode=hardwarecode)
    playerbaseinfo.SetPassword(pwd)
    db.session.add(playerbaseinfo)
    db.session.commit()
    return playerbaseinfo


@baseinfomodify.route('/register/002',methods=['GET','POST'])
def AddPlayer_002():
    DataBaseResponse = {'code': 1, 'ErrorMessage': 'Register Failed'}
    ClientRequest = request.get_json()
    if 'PlayerName' in ClientRequest:
        PlayerName = ClientRequest['PlayerName']
    else:
        return jsonify(DataBaseResponse)
    if 'BaseID' in ClientRequest:
        PlayerBaseID = ClientRequest['BaseID']
    else:
        return jsonify(DataBaseResponse)

    tpbaseinfo=PyGetBaseAccount_ID(PlayerBaseID)
    if(bool(tpbaseinfo)):
        if(not bool(tpbaseinfo.Account_002)):
            PyAddPlayer_002(PlayerBaseID,PlayerName)
            DataBaseResponse={'code': 200, 'ErrorMessage': 'Register Success', 'data': {}}
        else:
            DataBaseResponse['ErrorMessage']='Existing Account!'
    else:
        DataBaseResponse['ErrorMessage']='Invalid BaseAccount!'

    return jsonify(DataBaseResponse)


def PyAddPlayer_002(baseid, playername):
    playerbaseinfo = PlayerBase.query.get(baseid)
    TpPlayer002 = PyUnsafeAddPlayer_002(playername)
    playerbaseinfo.Account_002.append(TpPlayer002)
    db.session.merge(playerbaseinfo)
    db.session.commit()
    return TpPlayer002


'''
@baseinfomodify.route('addplayer004/<baseid>/<playername>/<hardwarecode>')
def AddPlayer_004(baseid,playername,hardwarecode):
    \'''
    Add player 004
    :param baseid: player base id
    :param playername: player name
    :return: player_004 json
    \'''
    return jsonify(PyAddPlayer_004(baseid,playername,hardwarecode).to_json())



def PyAddPlayer_004(baseid,playername,hardwarecode):
    playerbaseinfo=PlayerBase.query.get(baseid)
    TpPlayer004=PyUnsafeAddPlayer_004(playername,hardwarecode)
    playerbaseinfo.Account_004.append(TpPlayer004)
    db.session.merge(playerbaseinfo)
    db.session.commit()
    return TpPlayer004
'''


@baseinfomodify.route('/login',methods=['GET','POST'])
def LoginPlayerBase():
    DataBaseResponse = {'code': 1, 'ErrorMessage': 'Register Failed'}
    ClientRequest = request.get_json()
    if 'BaseID' in ClientRequest:
        PlayerBaseID = ClientRequest['BaseID']
    else:
        return jsonify(DataBaseResponse)
    if 'BaseName' in ClientRequest:
        BaseName = ClientRequest['BaseName']
    else:
        return jsonify(DataBaseResponse)
    if 'Password' in ClientRequest:
        BasePassword = ClientRequest['Password']
    else:
        return jsonify(DataBaseResponse)
    if 'HardwareCode' in ClientRequest:
        PlayerHardwareCode = ClientRequest['HardwareCode']
    else:
        return jsonify(DataBaseResponse)

    TpBaseInfo=PyFind_Name_Base(BaseName)
    if(TpBaseInfo):
        if(TpBaseInfo.CheckPassword(BasePassword)):
            if(not TpBaseInfo.BanStatus):
                if(TpBaseInfo.HardwareCode==PlayerHardwareCode):
                    DataBaseResponse = {'code': 200, 'ErrorMessage': 'Login Success', 'data': {'BaseID':TpBaseInfo.PlayerBaseID}}
                else:
                    DataBaseResponse['ErrorMessage']='New Computer! Do additional verification please!'
            else:
                DataBaseResponse['ErrorMessage']='The Account has been banned!'
        else:
            DataBaseResponse['ErrorMessage']='Invalid Password!'
    else:
        DataBaseResponse['ErrorMessage']='Invalid BaseName!'

    return jsonify(DataBaseResponse)

def PyGetBaseAccount_ID(id):
    return PlayerBase.query.get(id)

def PyFind_Name_Base(playername):
    return PlayerBase.query.filter_by(PlayerBaseName=playername).first()

@baseinfomodify.route('/verification',methods=['GET','POST'])
def TelephoneVerification():
    return