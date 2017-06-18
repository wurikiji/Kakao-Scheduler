import pyrebase

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

def loginFirebase() :
    firebase = pyrebase.initialize_app(config)
    return firebase
