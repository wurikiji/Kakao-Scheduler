import json,datetime,sys,logging,logging.handlers,re

def getJsonData(request):
    return json.loads(((request.body).decode('utf-8')))
