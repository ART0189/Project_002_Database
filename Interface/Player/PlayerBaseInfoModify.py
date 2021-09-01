from DataBase import db
from flask import Blueprint, jsonify
from Models.Player.PlayerBaseInfo import PlayerBase
from Interface.Player.PlayerModify_002 import *
from Interface.Player.PlayerModify_004 import *
from Interface.HardwareCodeCal import GetHardwareCode

baseinfomodify = Blueprint('baseinfomodify', __name__)


@baseinfomodify.route('/add/<basename>/<pwd>/<tele>')
def AddPlayerBase(basename, pwd, tele):
    return jsonify(PyAddPlayerBase(basename, pwd, tele).to_json())


def PyAddPlayerBase(basename, pwd, tele):
    playerbaseinfo = PlayerBase(PlayerBaseName=basename,Telephone=tele)
    playerbaseinfo.SetPassword(pwd)
    db.session.add(playerbaseinfo)
    db.session.commit()
    return playerbaseinfo


@baseinfomodify.route('/addplayer002/<baseid>/<playername>/<hardwarecode>')
def AddPlayer_002(baseid, playername,hardwarecode):
    '''
    Add player 002
    :param baseid: player base id
    :param playername: player name
    :return: player_002 json
    '''
    return jsonify(PyAddPlayer_002(baseid, playername,hardwarecode).to_json())


def PyAddPlayer_002(baseid, playername,hardwarecode):
    playerbaseinfo = PlayerBase.query.get(baseid)
    TpPlayer002 = PyUnsafeAddPlayer_002(playername,hardwarecode)
    playerbaseinfo.Account_002.append(TpPlayer002)
    db.session.merge(playerbaseinfo)
    db.session.commit()
    return TpPlayer002

@baseinfomodify.route('addplayer004/<baseid>/<playername>/<hardwarecode>')
def AddPlayer_004(baseid,playername,hardwarecode):
    '''
    Add player 004
    :param baseid: player base id
    :param playername: player name
    :return: player_004 json
    '''
    return jsonify(PyAddPlayer_004(baseid,playername,hardwarecode).to_json())

def PyAddPlayer_004(baseid,playername,hardwarecode):
    playerbaseinfo=PlayerBase.query.get(baseid)
    TpPlayer004=PyUnsafeAddPlayer_004(playername,hardwarecode)
    playerbaseinfo.Account_004.append(TpPlayer004)
    db.session.merge(playerbaseinfo)
    db.session.commit()
    return TpPlayer004
