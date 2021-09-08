import requests

BaseUrl = 'http://127.0.0.1:5000/'
AddUrl = ''
RequestData = {}


def RegisterBaseRequest(playername, password, telehone):
    AddUrl = 'baseinfomodify/register/base'
    RequestData = {'playername': playername, 'password': password, 'telephone': telehone}
    RequestHandle = requests.post(BaseUrl + AddUrl, data=RequestData, timeout=200)
    if (RequestHandle.status_code == 200):
        return 1,RequestHandle.content['baseid'],"ErrorMessage"
    else:
        return 0,-1,"ErrorMessage"


def Register002Request(playername, playerbaseid, hardwarecode):
    AddUrl = 'baseinfomodify/register/002'
    RequestData = {'playername': playername, 'baseid': playerbaseid, 'hardwarecode': hardwarecode}
    RequestHandle = requests.post(BaseUrl + AddUrl, data=RequestData, timeout=200)
    if (RequestHandle.status_code == 200):
        return 1,"ErrorMessage"
    else:
        return 0,"ErrorMessage"

def LoginBaseRequest(baseid,playername,password,hardwarecode):
    AddUrl = 'baseinfomodify/login'
    RequestData={'baseid':baseid,'basename':playername,'password':password,'hardwarecode':hardwarecode}
    RequestHandle=requests.post(BaseUrl+AddUrl,data=RequestData,timeout=200)
    if(RequestHandle.status_code==200):
        return 1,RequestHandle.content['baseid'],"ErrorMessage"
    else:
        return 0,-1,"ErrorMessage"

def Login002Request(playername, hardwarecode):
    AddUrl = 'playermodify002/login'
    RequestData = {'playername': playername, 'hardwarecode': hardwarecode}
    RequestHandle = requests.post(BaseUrl + AddUrl, data=RequestData, timeout=200)
    if (RequestHandle.status_code == 200):
        return 1,"ErrorMessage"
    else:
        return 0,"ErrorMessage"
