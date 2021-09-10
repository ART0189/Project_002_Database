from DataBase import db
from ..ModelsEntity import EntityBase

class TelephoneBanned(db.Model, EntityBase):
    __tablename__ = 'BaseBanned_Telephone'

    BanID=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    TelephoneBanned=db.Column(db.String(20), nullable=False)
