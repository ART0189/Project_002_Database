import requests

BaseUrl = 'http://127.0.0.1:5000/'
AddUrl = ''
RequestData = {}


def RegisterBaseRequest(playername, password, telehone):
    AddUrl = 'baseinfomodify/register/base'
    RequestData = {'playername': playername, 'password': password, 'telephone': telehone}
    RequestHandle = requests.post(BaseUrl + AddUrl, data=RequestData, timeout=200)
    if (RequestHandle.status_code == 200):
        return True
    else:
        return False


def Register002Request(playername, playerbaseid, hardwarecode):
    AddUrl = 'baseinfomodify/register/002'
    RequestData = {'playername': playername, 'baseid': playerbaseid, 'hardwarecode': hardwarecode}
    RequestHandle = requests.post(BaseUrl + AddUrl, data=RequestData, timeout=200)
    if (RequestHandle.status_code == 200):
        return True
    else:
        return False


def Login002Request(playername, hardwarecode):
    AddUrl = 'playermodify002/login'
    RequestData = {'playername': playername, 'hardwarecode': hardwarecode}
    RequestHandle = requests.post(BaseUrl + AddUrl, data=RequestData, timeout=200)
    if (RequestHandle.status_code == 200):
        return True
    else:
        return False
