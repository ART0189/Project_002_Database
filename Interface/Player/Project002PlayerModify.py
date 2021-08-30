from DataBase import db
from flask import Blueprint, jsonify
from Models.Player.Project002Player import Project002Player

playermodify_002 = Blueprint('playermodify002', __name__)

@playermodify_002.route('/add/<playername>')
def UnsafeAddPlayer_002(playername,hardwarecode):
    '''
    You shouldn't use it! Add any player of any project in player base info modify
    :param playername: player name
    :return: player_002 obj
    '''
    return jsonify(PyUnsafeAddPlayer_002(playername,hardwarecode).to_json())

def PyUnsafeAddPlayer_002(playername,hardwarecode):
    '''
    You shouldn't use it! Add any player of any project in player base info modify
    :param playername: player name
    :return: player_002 obj
    '''
    player_002 = Project002Player(Playername=playername,HardwareCode=hardwarecode)
    db.session.add(player_002)
    db.session.commit()
    return player_002
