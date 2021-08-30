from DataBase import db
import Interface.Player.PlayerBaseInfoModify as basem

def ConstructTest():
    TpPlayerBase = basem.PyAddPlayerBase('ART0189','123456','18302318793')
    basem.PyAddPlayer_002(TpPlayerBase.PlayerBaseID,'Ayanami')

    TpPlayerBase = basem.PyAddPlayerBase('Aressions', '1919810','114514')
    basem.PyAddPlayer_002(TpPlayerBase.PlayerBaseID, 'Aression')