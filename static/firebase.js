'use strict';
// for firebase-chat storage
// Initialize Firebase
var config = {
apiKey: "AIzaSyCpPmAc8T4ZbRF9ye3d0i5CQmGlln9h5GY",
		authDomain: "friendlychat-63958.firebaseapp.com",
		databaseURL: "https://friendlychat-63958.firebaseio.com",
		storageBucket: "friendlychat-63958.appspot.com",
		messagingSenderId: "51138195849"
};
var app = firebase.initializeApp(config);
var auth = app.auth();
var user = auth.currentUser;
var googleProvider = new firebase.auth.GoogleAuthProvider();
if (user == null) {
	auth.signInWithPopup(googleProvider).then(function(result) {
	/*
		user.displayName : user name
		user.email : user email
		user.emailVerified : verified or not (true/false)
		user.isAnonymous : true / false
		user.photoURL : user photo
	*/
		var user = result.user;
		$('body').append(user.displayName);
	}, function(error) {
		if (error.code === 'auth/popup-closed-by-user') {
			alert("You closed the login popup without signing-in.");
		} else if (error.code == 'auth/popup-blocked') {
			alert("Popup is blocked.");
		}
	});
} else {
	alert("Currently user " + user.displayName + " is in.");
}
