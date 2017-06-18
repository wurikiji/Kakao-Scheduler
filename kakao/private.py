# coding: utf-8
from kakao.firebase import * 
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

firebase = loginFirebase();
db = firebase.database()

def createGroup(userKey, userData):
    db.child('menuGroup').child(userData[0]).set({"pw":userData[1]})
    ret = "You created group '" + userData[0] + "' with password '" + userData[1] + "'."
    return ret

def loginGroupLow(userKey, userData):
    group = db.child('menuGroup').child(userData[0]).get()
    data = group.val()

    if data['pw'] == userData[1]:
        db.child('currentGroup').child(userKey).update({"group":userData[0]})
        return "You logged in to '" + userData[0] + "'."
    else :
        return "Password mismatched."


def loginGroup(userKey, ctype, content):
    result = {
        "message" : {
            "text" : "",
        },
    }
    userData = content.split()
    userData[0] = userData[0].split('#')[1]

    if len(userData) < 2:
        result['message']['text'] = "Type group password"
        return result

    if userData[0][0] == '#':
        result['message']['text'] = "Group name can not start with '#'"
        return result
    
    print userData
    user = db.child('menuGroup').child(userData[0]).get()
    data = user.val()
    
    if data:
        result['message']['text'] = loginGroupLow(userKey, userData)
    else:
        result['message']['text'] = createGroup(userKey, userData)

    return result

                                                                                            
def checkGroup(userKey):
    user = db.child('currentGroup').child(userKey).get()
    data = user.val()

    if data:
        return data['group']
    else :
        return '#'

def privateMenu(userKey, ctype, content):
    result = {
        "message" : {
            "text" : "기본 응답입니다.",
        },
    }

    content = content.split()

    command = content[0]
    menu = ""
    if len(content) > 1:
        for m in content[1:]:
            menu = menu + m

    group = checkGroup(userKey)
    if group == '#':
        result['message']['text'] = "You should log in to a group first."
        return result

    now = datetime.now()
    today = "%04d-%02d-%02d" % (now.year, now.month, now.day)

    printHelp = False
    ret = "기본응답"
    if "@l" == command:
        if len(menu) > 0:
            db.child('lunchMenu').child(group).child(today).set({userKey:menu})
            ret = "You added today's lunch menu " + menu
        else:
            printHelp = True
    elif "@d" == command:
        if len(menu) > 0:
            db.child('dinnerMenu').child(group).child(today).set({userKey:menu})
            ret = "You added today's dinner menu " + menu
        else:
            printHelp = True
    elif "@cl" == command:                                                                   
        data = db.child('lunchMenu').child(group).child(today).get()
    elif "@cd" == command:
        data = db.child('dinnerMenu').child(group).child(today).get()
    elif "@pl" == command:
        data = db.child('lunchMenu').child(group).child(today).get()
        ret = "Lunch Lists\n" 
        for menu in data.each():
            ret = ret + menu.val() + "/"
    elif "@pd" == command:
        data = db.child('dinnerMenu').child(group).child(today).get()
        ret = "Dinner Lists\n" 
        for menu in data.each():
            ret = ret + menu.val() + "/"
    else :                                                                                  
        printHelp = True

    if printHelp:
        result['message']['text'] = """This command is for private users only.
Type '#YourGroupName YourGroupPasswd' first.
'@l menu' - Add menu to lunch
'@d menu' - Add menu to dinner
'@cl' or '@cd' - Randomly choose menu from lunch/dinner lists
'@pl' or '@pc' - Print lunch/dinner lists"""
    else :
        result['message']['text'] = ret

    return result                                                                           
