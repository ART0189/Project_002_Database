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

    # Bind
    SourceBaseAccount = db.Column(db.INTEGER, db.ForeignKey('PlayerBaseData.PlayerBaseID'))
