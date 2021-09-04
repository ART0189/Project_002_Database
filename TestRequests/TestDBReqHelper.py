import requests

BaseUrl = 'http://127.0.0.1:5000/'
AddUrl=''
RequestData={}

def FindRequest(playername,hardwarecode):
    AddUrl='playermodify002/find'
    RequestData={'playername':playername,'hardwarecode':hardwarecode}
    RequestHandle=requests.post(BaseUrl+AddUrl,data=RequestData,timeout=200)
    if(RequestHandle.status_code==200):
        return True
    else:
        return False