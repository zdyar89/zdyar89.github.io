// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyCg3x9zhKtGQp37WxNxZX5C-HrEK3Dv-yQ",
  authDomain: "smartnotes-ddc24.firebaseapp.com",
  databaseURL: "https://smartnotes-ddc24.firebaseio.com",
  projectId: "smartnotes-ddc24",
  storageBucket: "smartnotes-ddc24.appspot.com",
  messagingSenderId: "756236356692",
  appId: "1:756236356692:web:7dfa8341bb533e664071c1",
  measurementId: "G-77ZFSKNZC0"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

var provider = new firebase.auth.GoogleAuthProvider();

function googleSignin() {
  firebase
    .auth()

    .signInWithPopup(provider)
    .then(function(result) {
      var token = result.credential.accessToken;
      var user = result.user;

      console.log(token);
      console.log(user);
    })
    .catch(function(error) {
      var errorCode = error.code;
      var errorMessage = error.message;

      console.log(error.code);
      console.log(error.message);
    });
}

function googleSignout() {
  firebase
    .auth()
    .signOut()

    .then(
      function() {
        console.log("Signout Succesfull");
      },
      function(error) {
        console.log("Signout Failed");
      }
    );
}
