from DataBase import db
from ..ModelsEntity import EntityBase

class HardwareCodeBanned(db.Model, EntityBase):
    __tablename__ = 'BaseBanned_HardwareCode'

    HardwareCodeBanned=db.Column(db.String(256), nullable=False)
