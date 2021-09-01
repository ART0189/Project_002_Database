from DataBase import db
from flask import Blueprint, jsonify
from Models.Player.Player_004 import Player_004

playermodify_004 = Blueprint('playermodify_004', __name__)


@playermodify_004.route('/add/<playername>')
def UnsafeAddPlayer_004(playername, hardwarecode):
    '''
    You shouldn't use it! Add any player of any project in player base info modify
    :param playername: player name
    :return: player_004 json
    '''
    return jsonify(PyUnsafeAddPlayer_004(playername, hardwarecode).to_json())


def PyUnsafeAddPlayer_004(playername, hardwarecode):
    '''
    You shouldn't use it! Add any player of any project in player base info modify
    :param playername: player name
    :return: player_004 obj
    '''
    player_004 = Player_004(PlayerName=playername, HardwareCodd=hardwarecode)
    db.session.add(player_004)
    db.session.commit()
    return player_004
