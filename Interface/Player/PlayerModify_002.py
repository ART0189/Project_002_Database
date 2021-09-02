from DataBase import db
from flask import Blueprint, jsonify
from Models.Player.Player_002 import Player_002

playermodify_002 = Blueprint('playermodify002', __name__)

@playermodify_002.route('/add/<playername>')
def UnsafeAddPlayer_002(playername,hardwarecode):
    '''
    You shouldn't use it! Add any player of any project in player base info modify
    :param playername: player name
    :return: player_002 json
    '''
    return jsonify(PyUnsafeAddPlayer_002(playername,hardwarecode).to_json())

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

def PyFind_ID_002(playerid):
    return Player_002.query.get(playerid)

def PyFind_Name_002(playername):
    return Player_002.query.filter_by(PlayerName=playername).first()

def PyCheckPlayer_002(playername,hardwarecode):
    return PyFind_Name_002(playername).HardwareCode==hardwarecode