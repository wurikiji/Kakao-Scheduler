from django.http import JsonResponse 
from kakao.getjson import *
from kakao.firebase import * 
from kakao.private import * 

firebase = loginFirebase();

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
    user = db.child("schedulerAccounts").child(userKey).get()
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
    "type" : "text",
}

kakaoCommands2= {
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
        },
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
    "@" : privateMenu,
    "#" : loginGroup,
}

def getResult(userKey, ctype, content):
    result = {
        "message" : {
            "text" : "Thank you for your image :).",
        }
    }
    if (ctype == "text") :
        command = content
        if content[0] == '#' or content[0] == '@':
            command = content[0]

        func = funcDict.get(command.lower(), defaultAnswer)
        result = func(userKey, ctype, content)

    return JsonResponse(result)
