from django.shortcuts import render
from django.shortcuts import render_to_response
from django import template
from django.template import RequestContext
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json,datetime,sys,logging,logging.handlers,re
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from kakao.answer import *
from kakao.getjson import *


# Create your views here.
# Default views for Home Keyboard API
# When users come into chat room at first, 
# "type":"test" -> Normal text input
# "type":"buttons" -> Button input 
#   {"type": "buttons",
#   "buttons" : ["Button1", "button2", "Button3"]}
#

def keyboard(request):
    
	return JsonResponse(kakaoCommands)
	#return JsonResponse({ "type":"text", })

@csrf_exempt
def leaveRoom(request, user_key):
    print "User key is " + user_key
    return JsonResponse({})

# user_key: user unique id
# type: "text", "photo"
# content: text or photo url
@csrf_exempt
def answer(request):
    data = getJsonData(request)
    userKey = data['user_key']
    ctype = data['type']
    content = data['content']
    return getResult(userKey, ctype, content)
#{
#  "message": {
#    "text": "!",
#    "photo": {
#      "url": "https://photo.src",
#      "width": 640,
#      "height": 480
#    },
#    "message_button": {
#      "label": "",
#      "url": "https://coupon/url"
#    }
#  },
#  "keyboard": {
#    "type": "buttons",
#    "buttons": [
#      "",
#      "",:
#      ""
#    ]
#  }
#}

@csrf_exempt
def add_friend(request):
    data = getJsonData(request)
    print "Add user"
    return JsonResponse({})

@csrf_exempt
def del_friend(request, user_key):
    print "Remove user"
    return JsonResponse({})

def index(request):
	return render(request, 'index.html',)

def loginWithKey(request, userKey):
    ctx = {"key": str(userKey)}
    return render(request, 'login.html', ctx)
                
