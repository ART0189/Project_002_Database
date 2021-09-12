from DataBase import db
from flask import Blueprint, jsonify, request
from Models.Player.Player_002 import Player_002
import Interface.Player.PlayerBaseInfoModify as BM

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
    DataBaseResponse={'code':1,'ErrorMessage':'Find Failed','data':{}}
    ClientRequest=request.get_json()
    if 'BaseID' in ClientRequest:
        BaseID=ClientRequest['BaseID']
    else:
        return jsonify(DataBaseResponse)
    if 'HardwareCode' in ClientRequest:
        PlayerHardwareCode=ClientRequest['HardwareCode']
    else:
        return jsonify(DataBaseResponse)

    tpbaseinfo=BM.PyGetBaseAccount_ID(BaseID)
    if(tpbaseinfo):
        PlayerInfo=tpbaseinfo.Account_002[0]
        if(PlayerInfo):
            if(not tpbaseinfo.BanStatus):
                if(tpbaseinfo.HardwareCode==PlayerHardwareCode):
                    DataBaseResponse['code']=200
                    DataBaseResponse['ErrorMessage']='Find Success'
                    DataBaseResponse['data']=PyConstructAccount002Helper(PlayerInfo)
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

def PyConstructAccount002Helper(Account002):
    TpRetStruct={}
    TpRetStruct['PlayerID']=Account002.PlayerID
    TpRetStruct['PlayerName']=Account002.PlayerName
    TpRetStruct['HeadPortrait']=Account002.HeadPortrait
    TpRetStruct['PlayerLv']=Account002.PlayerLv
    TpRetStruct['PlayerExp']=Account002.PlayerExp
    TpRetStruct['PlayerRank']=Account002.PlayerRank
    TpRetStruct['PlayerToken']=Account002.PlayerToken
    TpRetStruct['PlayerToken_1']=Account002.PlayerToken_1
    TpRetStruct['PlayerDefaultOOBName']=Account002.PlayerDefaultOOBName

    return TpRetStruct