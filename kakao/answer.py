from django.http import JsonResponse 
import pyrebase
from kakao.getjson import *


STR_VERIFY = "Verify"
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

def signInWithGoogle(userKey, ctype, content):
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
def verify(userKey, ctype, content): 
    result = {
        "message" : {
            "text" : "You did not log in.", 
        },
    }
    db = firebase.database()
    user = db.child("schedulerAccounts/" + userKey).get()
    data = user.val()
    if data:
        result = {
            "message" : {
                "text" : "Your email is " + data['userMail'] + "." +
                    " You succefully logged in.",
            },
        }
        

    return result

kakaoCommands= {
    "type" : "buttons",
    "buttons" : [
        "HELP", "LOGIN", "VERIFY",
        "?",
    ]
}

def showCommands(userKey, ctype, content) :
    ret = {
        "message" : {
            "text" : "Select one of the commands.",
        },
        "keyboard" : kakaoCommands    }
    return ret

def defaultAnswer(userKey, ctype, content): 
    result= {
        "message" : {
            "text" : "'" + content + "' is not a command. Type 'help' " + 
                    "to view the details." + 
                    "\nIf you hurry, use 1:1 chat service.", 
            "message_button" : {
                "label": "Go to Help",
                "url" : "https://github.com/wurikiji/Kakao-Scheduler",
            },
        },
        "keyboard" : {
            "type" : "buttons",
            "buttons": [
                "help",
                "?",
            ]
        }
    }
    if content.lower() == STR_IGNORE.lower():
        result = {
            "message" : {
                "text" : ";( ... Why?!",
            },
        }
    return result

def getHelp(userKey, ctype, content):
    result = {
        "message" : {
            "text" : "Type '?' to show commands.",
            "message_button" : {
                "label": "Go to Homepage",
                "url" : "https://github.com/wurikiji/Kakao-Scheduler",
            },
        },
        "keyboard" : {
            "type": "buttons",
            "buttons" : [
                "?", 
            ]
        }
    }
    return result

funcDict = {
    "?" : showCommands,
    STR_VERIFY.lower(): verify,
    STR_LOGIN.lower(): signInWithGoogle,
    "help" : getHelp,
}

def getResult(userKey, ctype, content):
    result = {
        "message" : {
            "text" : "Thank you for your image :).",
        }
    }
    if (ctype == "text") :
        func = funcDict.get(content.lower(), defaultAnswer)
        result = func(userKey, ctype, content)

    return JsonResponse(result)
