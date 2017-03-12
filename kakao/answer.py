from django.http import JsonResponse 
import pyrebase
from kakao.getjson import *


STR_VERIFY = "Verify Login"
STR_LOGIN = "login"
STR_IGNORE = "Ignore"

config = {
  "apiKey": "AIzaSyCpPmAc8T4ZbRF9ye3d0i5CQmGlln9h5GY",
  "authDomain": "friendlychat-63958.firebaseapp.com",
  "databaseURL": "https://friendlychat-63958.firebaseio.com",
  "storageBucket": "friendlychat-63958.appspot.com",
  "messagingSenderId": "51138195849",
  "serviceAccount": "/home/ogh/work/tapache/ogh/firebase-key.json",
}

firebase = pyrebase.initialize_app(config)

def signInWithGoogle(userKey, content):
    result = ""
    if ( STR_LOGIN.lower() == content.lower() ) :
        result = {
            "message" : {
                "text" : "Please, sign in with google id. Click button if you want to join." + 
                "\nAfter login, please verify your login.",
                "message_button": {
                    "label": "Sign in with Google ID",
                    "url": "https://35.187.195.27/" + userKey,
                },
            },
            "keyboard" : {
                "type": "buttons", 
                "buttons" : [
                    STR_VERIFY,
                    STR_IGNORE,
                ]
            }
        }
    return result 


# verify login with firebase
def verify(userKey): 
    result = {
        "message" : {
            "text" : "You did not log in.", 
        },
    }
    db = firebase.database()
    user = db.child("schedulerAccounts/" + userKey).get()
    data = user.val()
    if len(data) != 0:
        result = {
            "message" : {
                "text" : "Your email is " + data['userMail'] + "." +
                    " You succefully logged in.",
            },
        }
        

    return result

# get answer to users question 
def getAnswer(userKey, ctype, content): 
    result= {
        "message" : {
            "text" : content + " is not a command. 'login' is only supported.", 
        },
    }
    if content.lower() == STR_VERIFY.lower(): 
        print "Verifying user identification"
        result = verify(userKey)
    elif content.lower() == STR_IGNORE.lower():
        result = {
            "message" : {
                "text" : ";( ... Why?!",
            },
        }

    return result

def getResult(userKey, ctype, content):
    result = signInWithGoogle(userKey, content)

    if len(result) == 0 :
        result = getAnswer(userKey, ctype, content)

    return JsonResponse(result)
