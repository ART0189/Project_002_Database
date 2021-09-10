from DataBase import db
from ..ModelsEntity import EntityBase


class Player_002(db.Model, EntityBase):
    __tablename__ = 'PlayerData_Project002'

    # BaseInfo
    PlayerID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    PlayerName = db.Column(db.String(10), nullable=False)
    HeadPortrait = db.Column(db.String(100), nullable=False, default='NeedInit')
    PlayerLv = db.Column(db.INTEGER, nullable=False, default=0)
    PlayerExp = db.Column(db.INTEGER, nullable=False, default=0)
    HaveLogin = db.Column(db.Boolean, nullable=False, default=False)

    # Check

    # Bind
    SourceBaseAccount = db.Column(db.INTEGER, db.ForeignKey('PlayerBaseData.PlayerBaseID'))
