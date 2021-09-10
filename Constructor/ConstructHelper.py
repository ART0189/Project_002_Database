from DataBase import db
import Interface.Player.PlayerBaseInfoModify as basem
import Interface.Ban.BanModify as bm

def ConstructTest():
    TpPlayerBase = basem.PyAddPlayerBase('ART0189','123456','18302318793','UnInitedHardwareCode')
    basem.PyAddPlayer_002(TpPlayerBase.PlayerBaseID,'Ayanami')

    TpPlayerBase = basem.PyAddPlayerBase('Aressions', '1919810','114514','UnInitedHardwareCode')
    basem.PyAddPlayer_002(TpPlayerBase.PlayerBaseID, 'Aression')

    bm.PyAddTelephoneBanned('15123880949')