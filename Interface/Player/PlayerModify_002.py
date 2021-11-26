from DataBase import db
from flask import Blueprint, json, jsonify, request
from Models.Player.Player_002 import Player_002
from Interface.Player.PlayerBaseSimpleModify import *

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

    tpbaseinfo=PyGetBaseAccount_ID(BaseID)
    if(tpbaseinfo):
        PlayerInfo=tpbaseinfo.Account_002[0]
        if(PlayerInfo):
            if(not tpbaseinfo.BanStatus):
                if(tpbaseinfo.HardwareCode==PlayerHardwareCode):
                    DataBaseResponse['code']=200
                    DataBaseResponse['ErrorMessage']='Find Success'
                    DataBaseResponse['data']=PyMakeAccount002Struct(PlayerInfo)
                else:
                    DataBaseResponse['ErrorMessage']='New Computer! Do additional verification please!'
            else:
                DataBaseResponse['ErrorMessage']='The Account has been banned!'
        else:
            DataBaseResponse['ErrorMessage']='The BaseAccount havent any Account002'
    else:
        DataBaseResponse['ErrorMessage']='Invalid BaseAccount!'

    return jsonify(DataBaseResponse)

@playermodify_002.route('/friend/request',methods=['GET','POST'])
def RequestFriend002():
    DataBaseResponse={'code':1,'ErrorMessage':'Find Failed','data':{}}
    ClientRequest=request.get_json()
    if 'PlayersID' in ClientRequest:
        PlayerID=ClientRequest['PlayersID']
    else:
        return jsonify(DataBaseResponse)

    tpplayerinfo=PyGet002_ID(PlayerID)
    if(tpplayerinfo):
        DataBaseResponse['code']=200
        DataBaseResponse['ErrorMessage']='Request Success'
        TpFriendsInfoList=PyGetFriendStructFourParams(tpplayerinfo.FriendsList)
        DataBaseResponse['data']={'FriendsID':TpFriendsInfoList[0],'FriendsName':TpFriendsInfoList[1],'FriendsHeadPortrait':TpFriendsInfoList[2],'FriendsLv':TpFriendsInfoList[3]}
    else:
        DataBaseResponse['ErrorMessage']='Invalid Player ID!'

    return jsonify(DataBaseResponse)

@playermodify_002.route('/friend/add',methods=['GET','POST'])
def AddFriend002():
    DataBaseResponse={'code':1,'ErrorMessage':'Find Failed','data':{}}
    ClientRequest=request.get_json()
    if 'PlayerID' in ClientRequest:
        PlayerID=ClientRequest['PlayerID']
    else:
        return jsonify(DataBaseResponse)
    if 'FriendID' in ClientRequest:
        FriendID=ClientRequest['FriendID']
    else:
        return jsonify(DataBaseResponse)

    tpplayerinfo=PyGet002_ID(PlayerID)
    if(tpplayerinfo):
        if(PyGet002_ID(FriendID)):
            DataBaseResponse['code']=200
            PyAddFriend002(PlayerID,FriendID)
            DataBaseResponse['ErrorMessage']='Add Success'
            TpFriendsInfoList=PyGetFriendStructFourParams(tpplayerinfo.FriendsList)
            DataBaseResponse['data']={'FriendsID':TpFriendsInfoList[0],'FriendsName':TpFriendsInfoList[1],'FriendsHeadPortrait':TpFriendsInfoList[2],'FriendsLv':TpFriendsInfoList[3]}
        else:
            DataBaseResponse['ErrorMessage']='Invalid Friend ID!'
    else:
        DataBaseResponse['ErrorMessage']='Invalid Player ID!'

    return jsonify(DataBaseResponse)

@playermodify_002.route('/friend/delete',methods=['GET','POST'])
def DeleteFriend002():
    DataBaseResponse={'code':1,'ErrorMessage':'Find Failed','data':{}}
    ClientRequest=request.get_json()
    if 'PlayerID' in ClientRequest:
        PlayerID=ClientRequest['PlayerID']
    else:
        return jsonify(DataBaseResponse)
    if 'FriendID' in ClientRequest:
        FriendID=ClientRequest['FriendID']
    else:
        return jsonify(DataBaseResponse)

    tpplayerinfo=PyGet002_ID(PlayerID)
    if(tpplayerinfo):
        if(PyGet002_ID(FriendID)):
            PyDeleteFriend002(PlayerID,FriendID)
            DataBaseResponse['code']=200
            DataBaseResponse['ErrorMessage']='Delete Success'
            TpFriendsInfoList=PyGetFriendStructFourParams(tpplayerinfo.FriendsList)
            DataBaseResponse['data']={'FriendsID':TpFriendsInfoList[0],'FriendsName':TpFriendsInfoList[1],'FriendsHeadPortrait':TpFriendsInfoList[2],'FriendsLv':TpFriendsInfoList[3]}
        else:
            DataBaseResponse['ErrorMessage']='Invalid Friend ID!'
    else:
        DataBaseResponse['ErrorMessage']='Invalid Player ID!'

    return jsonify(DataBaseResponse)

@playermodify_002.route('/playerinfo',methods=['GET','POST'])
def GetPlayerSimpleInfo():
    DataBaseResponse={'code':1,'ErrorMessage':'Find Failed','data':{}}
    ClientRequest=request.get_json()
    if 'PlayerID' in ClientRequest:
        PlayerID=ClientRequest['PlayerID']
    else:
        return jsonify(DataBaseResponse)

    tpplayerinfo=PyGet002_ID(PlayerID)
    if(tpplayerinfo):
        DataBaseResponse['code']=200
        DataBaseResponse['ErrorMessage']='Get Success'
        DataBaseResponse['data']={'PlayerInfoStr':PyMakeSimplePlayerinfo002(tpplayerinfo)}
    else:
        DataBaseResponse['ErrorMessage']='Invalid Player ID!'

    return jsonify(DataBaseResponse)

@playermodify_002.route('/request/players',methods=['GET','POST'])
def RequestPlayer002():
    DataBaseResponse={'code':1,'ErrorMessage':'Find Failed','data':{}}
    ClientRequest=request.get_json()
    if 'PlayersID' in ClientRequest:
        PlayersID=ClientRequest['PlayersID']
    else:
        return jsonify(DataBaseResponse)

    DataBaseResponse['code']=200
    DataBaseResponse['ErrorMessage']='Request Success'
    TpPlayersInfoList=PyGetFriendStructFourParams(PlayersID)
    DataBaseResponse['data']={'PlayersID':TpPlayersInfoList[0],'PlayersName':TpPlayersInfoList[1],'PlayersHeadPortrait':TpPlayersInfoList[2],'PlayersLv':TpPlayersInfoList[3]}

    return jsonify(DataBaseResponse)

def PyAddFriend002(playerid,friendid):
    return PyGet002_ID(playerid).AddFriend(friendid)

def PyDeleteFriend002(playerid,friendid):
    PyGet002_ID(playerid).DeleteFriend(friendid)

def PyGet002_ID(playerid):
    return Player_002.query.get(playerid)

def PyFind_Name_002(playername):
    return Player_002.query.filter_by(PlayerName=playername).first()

def PyMakeAccount002Struct(Account002):
    TpRetStruct={}
    TpRetStruct['PlayerID']=Account002.PlayerID
    TpRetStruct['PlayerName']=Account002.PlayerName
    TpRetStruct['HeadPortrait']=Account002.HeadPortrait
    TpRetStruct['PlayerLv']=Account002.PlayerLv
    TpRetStruct['PlayerExp']=Account002.PlayerExp
    TpRetStruct['PlayerRank']=Account002.PlayerRank
    TpRetStruct['PlayerToken']=[Account002.PlayerToken,Account002.PlayerToken1]
    TpRetStruct['PlayerDefaultOOBName']=Account002.PlayerDefaultOOBName

    return TpRetStruct

def PyMakeFriendStruct(Account002):
    TpRetStruct={}
    TpRetStruct['PlayerID']=Account002.PlayerID
    TpRetStruct['PlayerName']=Account002.PlayerName
    TpRetStruct['HeadPortrait']=Account002.HeadPortrait
    TpRetStruct['PlayerLv']=Account002.PlayerLv
    TpRetStruct['PlayerRank']=Account002.PlayerRank

    return TpRetStruct

def PyGetFriendStructFourParams(PlayersIDList):
    TpFriendIDListStr=''
    TpFriendNameListStr=''
    TpFriendHeadPortraitListStr=''
    TpFriendLvListStr=''

    PlayersIDList=PlayersIDList.split(',')
    PlayersIDList.pop()
    
    for i in PlayersIDList:
        TpFriendInfoStruct=PyMakeFriendStruct(PyGet002_ID(i))
        if(not bool(TpFriendInfoStruct)):
            continue

        TpFriendIDListStr+=str(TpFriendInfoStruct['PlayerID'])
        TpFriendIDListStr+=','

        TpFriendNameListStr+=str(TpFriendInfoStruct['PlayerName'])
        TpFriendNameListStr+=','

        TpFriendHeadPortraitListStr+=str(TpFriendInfoStruct['HeadPortrait'])
        TpFriendHeadPortraitListStr+=','

        TpFriendLvListStr+=str(TpFriendInfoStruct['PlayerLv'])
        TpFriendLvListStr+=','

    return TpFriendIDListStr,TpFriendNameListStr,TpFriendHeadPortraitListStr,TpFriendLvListStr

def PyMakeSimplePlayerinfo002(Account002):
    TpRetStr=''

    TpRetStr+=str(Account002.PlayerID)
    TpRetStr+=','

    TpRetStr+=str(Account002.PlayerName)
    TpRetStr+=','

    TpRetStr+=str(Account002.HeadPortrait)
    TpRetStr+=','

    TpRetStr+=str(Account002.PlayerLv)
    TpRetStr+=','

    TpRetStr+=str(Account002.PlayerRank)
    TpRetStr+=','

    return TpRetStr