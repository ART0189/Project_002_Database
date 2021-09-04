from DataBase import db
from ..ModelsEntity import EntityBase


class PlayerBase(db.Model, EntityBase):
    __tablename__ = 'PlayerBaseData'

    # NaturalPerson
    PlayerBaseID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    PlayerBaseName = db.Column(db.String(15), nullable=False)
    _Password = db.Column(db.String(20), nullable=False)
    Gender = db.Column(db.Enum('男', '女', '其他', '未知'), nullable=False, default='未知')

    def SetPassword(self, InputPassword):
        self._Password = InputPassword
        return True

    def CheckPassword(self, InputPassword):
        return InputPassword == self._Password

    # StaticInfo
    HeadPortrait = db.Column(db.String(100), nullable=False, default='DefaultPath')
    Address = db.Column(db.String(50), nullable=False,default='Home')
    Telephone = db.Column(db.String(20), nullable=False)

    # DynamicInfo
    _HaveLogin = db.Column(db.Boolean, default=False)

    def Login(self):
        if (not self._HaveLogin):
            self._HaveLogin = not self._HaveLogin

        return not self._HaveLogin

    def Exit(self):
        if (self._HaveLogin):
            self._HaveLogin = not self._HaveLogin

        return self._HaveLogin

    def LoginStatus(self):
        return self._HaveLogin

    # PlayerBind
    Account_002 = db.relationship('Player_002', backref='PlayerBaseData')
    Account_004 = db.relationship('Player_004', backref='PlayerBaseData')
