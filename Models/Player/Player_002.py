from DataBase import db
from ..ModelsEntity import EntityBase


class Player_002(db.Model, EntityBase):
    __tablename__ = 'PlayerData_Project002'

    # BaseInfo
    PlayerID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    PlayerName = db.Column(db.String(10), nullable=False)
    HeadPortrait = db.Column(db.INTEGER, nullable=False, default=1)
    PlayerLv = db.Column(db.INTEGER, nullable=False, default=0)
    PlayerExp = db.Column(db.INTEGER, nullable=False, default=0)
    PlayerRank = db.Column(db.String(10))
    PlayerToken = db.Column(db.INTEGER,nullable=False,default=0)
    PlayerToken_1 = db.Column(db.INTEGER,nullable=False,default=0)
    PlayerDefaultOOBName = db.Column(db.String(10))
    HaveLogin = db.Column(db.Boolean, nullable=False, default=False)

    # Check

    # Firends
    FriendsList=db.Column(db.String(1000),default='')    # Divide ID by ','

    def AddFriend(self,NewID):
        '''
        Ret if add succeeded
        '''
        if(not self.FindFriendHelper(NewID)):
            try:
                self.FriendsList+=str(NewID)
                self.FriendsList+=','
            except:
                return False
            return True
        else:
            return False

    def DeleteFriend(self,DeleteID):
        '''
        Void no Ret
        '''
        IDList=self.FriendsList.split(',')
        IDList.remove(DeleteID)


    def FindFriendHelper(self,TargetID):
        '''
        Ret if find TargetID, if true return index
        '''
        IDList=self.FriendsList.split(',')
        for i in IDList:
            if(i==str(TargetID)):
                return True
        
        return False


    # Bind
    SourceBaseAccount = db.Column(db.INTEGER, db.ForeignKey('PlayerBaseData.PlayerBaseID'))
