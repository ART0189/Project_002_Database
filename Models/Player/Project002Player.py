from DataBase import db
from ..ModelsEntity import EntityBase


class Project002Player(db.Model, EntityBase):
    __tablename__ = 'PlayerData_Project002'

    # BaseInfo
    PlayerID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    Playername = db.Column(db.String(10), nullable=False)
    HeadPortrait = db.Column(db.String(100), nullable=False, default='NeedInit')
    PlayerLv = db.Column(db.INTEGER, nullable=False, default=0)
    PlayerExp = db.Column(db.INTEGER, nullable=False, default=0)
    HaveLogin = db.Column(db.Boolean, nullable=False, default=False)

    # Check
    HardwareCode = db.Column(db.String(256), nullable=False)

    # Bind
    SourceBaseAccount = db.Column(db.INTEGER, db.ForeignKey('PlayerBaseData.PlayerBaseID'))
