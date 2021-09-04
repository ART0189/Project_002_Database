from DataBase import db
from flask import Blueprint, jsonify, request
from Models.Player.PlayerBaseInfo import PlayerBase
from Interface.Player.PlayerModify_002 import *
from Interface.Player.PlayerModify_004 import *
from Interface.HardwareCodeCal import GetHardwareCode

baseinfomodify = Blueprint('baseinfomodify', __name__)


@baseinfomodify.route('/register/base',methods=['GET','POST'])
def AddPlayerBase():
    DataBaseResponse = {'code': 1, 'message': 'Register Failed', 'data': {}}
    ClientRequest = request.values
    if 'playername' in ClientRequest:
        PlayerName = ClientRequest['playername']
    else:
        return jsonify(DataBaseResponse)
    if 'password' in ClientRequest:
        PlayerPassword = ClientRequest['password']
    else:
        return jsonify(DataBaseResponse)
    if 'telephone' in ClientRequest:
        PlayereTelephone = ClientRequest['telephone']
    else:
        return jsonify(DataBaseResponse)

    PlayerBaseInfo=PyAddPlayerBase(PlayerName,PlayerPassword,PlayereTelephone)
    DataBaseResponse={'code': 200, 'message': 'Register Success', 'data': {'baseid':PlayerBaseInfo.PlayerBaseID}}
    return jsonify(DataBaseResponse)


def PyAddPlayerBase(basename, pwd, tele):
    playerbaseinfo = PlayerBase(PlayerBaseName=basename,Telephone=tele)
    playerbaseinfo.SetPassword(pwd)
    db.session.add(playerbaseinfo)
    db.session.commit()
    return playerbaseinfo


@baseinfomodify.route('/register/002',methods=['GET','POST'])
def AddPlayer_002():
    DataBaseResponse = {'code': 1, 'message': 'Register Failed', 'data': {}}
    ClientRequest = request.values
    if 'playername' in ClientRequest:
        PlayerName = ClientRequest['playername']
    else:
        return jsonify(DataBaseResponse)
    if 'baseid' in ClientRequest:
        PlayerBaseID = ClientRequest['baseid']
    else:
        return jsonify(DataBaseResponse)
    if 'hardwarecode' in ClientRequest:
        PlayerHardwareCode = ClientRequest['hardwarecode']
    else:
        return jsonify(DataBaseResponse)

    PyAddPlayer_002(PlayerBaseID,PlayerName,PlayerHardwareCode)
    DataBaseResponse={'code': 200, 'message': 'Register Success', 'data': {}}
    return jsonify(DataBaseResponse)


def PyAddPlayer_002(baseid, playername,hardwarecode):
    playerbaseinfo = PlayerBase.query.get(baseid)
    TpPlayer002 = PyUnsafeAddPlayer_002(playername,hardwarecode)
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
'''


def PyAddPlayer_004(baseid,playername,hardwarecode):
    playerbaseinfo=PlayerBase.query.get(baseid)
    TpPlayer004=PyUnsafeAddPlayer_004(playername,hardwarecode)
    playerbaseinfo.Account_004.append(TpPlayer004)
    db.session.merge(playerbaseinfo)
    db.session.commit()
    return TpPlayer004
