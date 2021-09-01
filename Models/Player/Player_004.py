from DataBase import db
from ..ModelsEntity import EntityBase


class Player_004(db.Model, EntityBase):
    __tablename__ = 'PlayerData_Project002'

    # BaseInfo
    PlayerID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    PlayerName = db.Column(db.String(10), nullable=False)
    HaveLogin = db.Column(db.Boolean, nullable=False, default=False)

    # Check
    HardwareCode = db.Column(db.String(256), nullable=False)

    # Bind
    SourceBaseAccount = db.Column(db.INTEGER, db.ForeignKey('PlayerBaseData.PlayerBaseID'))
