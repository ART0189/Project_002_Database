from DataBase import db
from flask import Blueprint, jsonify
from Models.Player.PlayerBaseInfo import PlayerBase
from Interface.Player.Project002PlayerModify import *
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


@baseinfomodify.route('/addplayer002/<baseid>/<playername>')
def AddPlayer_002(baseid, playername):
    '''
    Add player 002
    :param playername: player name
    :return: player_002 obj
    '''
    return jsonify(PyAddPlayer_002(baseid, playername).to_json())


def PyAddPlayer_002(baseid, playername):
    playerbaseinfo = PlayerBase.query.get(baseid)
    TpPlayer002 = PyUnsafeAddPlayer_002(playername,GetHardwareCode())
    playerbaseinfo.Account_002.append(TpPlayer002)
    db.session.merge(playerbaseinfo)
    db.session.commit()
    return TpPlayer002
