from DataBase import db
from ..ModelsEntity import EntityBase

class TelephoneBanned(db.Model, EntityBase):
    __tablename__ = 'BaseBanned_Telephone'

    TelephoneBanned=db.Column(db.String(20), nullable=False)
