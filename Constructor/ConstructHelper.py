from DataBase import db
import random
import string
import datetime
import Interface.Player.PlayerBaseInfoModify as basem
import Interface.Player.PlayerModify_002 as pm002
import Interface.Ban.BanModify as banm

AccountNameList=['ART','ATRI','Ayanami','Poi','Shimakaze','Laffey','Yukikaze','LeMalin','Tashkent',
'Ingraham','Columbia','Mainz','Swiftsure','Noshiro','Azuma','Nagato','Alabama']


def ConstructAll(seed):
    random.seed(seed)
    Construct_BaseAccount(10)
    Construct_AccountData002(10)

def Construct_BaseAccount(AccountNum):
    for i in range(AccountNum):
        TpPlayerBase = basem.PyAddPlayerBase(RandomName(14),RandomPassword(True),RandomTelephone(),'UnInitedHardwareCode')
        basem.PyAddPlayer_002(TpPlayerBase.PlayerBaseID,RandomSimpleName())

def Construct_AccountData002(AccountNum,MaxHeadPortraitIndex=5,MaxLv=40,TokenLimit=[10000,50000],Token1Limit=[1000000, 90000000]):
    for i in range(AccountNum):
        tpinfo002=pm002.PyGet002_ID(i+1)
        tpinfo002.HeadPortrait=random.randint(0, MaxHeadPortraitIndex)
        tpinfo002.PlayerLv=random.randint(0, 40)
        tpinfo002.PlayerExp=random.randint(0, tpinfo002.PlayerLv*25+100)
        tpinfo002.PlayerToken=random.randint(TokenLimit[0], TokenLimit[1])
        tpinfo002.PlayerToken_1=random.randint(Token1Limit[0], Token1Limit[1])
        for i in range(random.randint(1, AccountNum)):
            tpinfo002.AddFriend(random.randint(1, AccountNum))

        db.session.merge(tpinfo002)
    db.session.commit()

def RandomName(MaxLen):
    SuffixLen=MaxLen-9
    MaxNum=10**SuffixLen-1
    return AccountNameList[random.randint(0, len(AccountNameList)-1)]+str(random.randint(0, MaxNum))

def RandomSimpleName():
    return AccountNameList[random.randint(0, len(AccountNameList)-1)]

def RandomPassword(BSimple):
    if(not BSimple):
        TpPwd = ''
        for i in range(20):
            TpSelect = random.randint(0, 3)
            if (TpSelect == 0):
                TpPwd += string.digits[random.randint(0, 9)]
            elif (TpSelect == 1):
                TpPwd += string.ascii_lowercase[random.randint(0, 25)]
            elif (TpSelect == 2):
                TpPwd += string.ascii_uppercase[random.randint(0, 25)]
            else:
                TpPwd += string.punctuation[random.randint(0, 30)]
    else:
        TpPwd='123456'

    return TpPwd

def RandomTelephone():
    '''
    Random telephone generator
    :return: telephone
    '''
    TeleBegin = [134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172, 178, 182, 183, 184, 187, 188,
                 195, 197, 198,
                 130, 131, 132, 145, 155, 156, 166, 175, 176, 185, 186, 196,
                 133, 149, 153, 180, 181, 189, 173, 177, 190, 191, 193, 199]
    TpTele = ''
    TpTele += str(TeleBegin[random.randint(0, len(TeleBegin) - 1)])
    for i in range(8):
        TpTele += string.digits[random.randint(0, 9)]

    return TpTele