from DataBase import db
from ..ModelsEntity import EntityBase

class HardwareCodeBanned(db.Model, EntityBase):
    __tablename__ = 'BaseBanned_HardwareCode'

    BanID=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    HardwareCodeBanned=db.Column(db.String(256), nullable=False)
