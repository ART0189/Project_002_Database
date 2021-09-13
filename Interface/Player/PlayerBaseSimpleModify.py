from Models.Player.PlayerBaseInfo import PlayerBase


def PyGetBaseAccount_ID(id):
    return PlayerBase.query.get(id)

def PyFind_Name_Base(playername):
    return PlayerBase.query.filter_by(PlayerBaseName=playername).first()