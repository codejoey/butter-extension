//service worker to catch any errors
try{
  //import local scripts
  self.importScripts('firebase/firebase-app.js', 'firebase/firebase-database.js');

  //your web app's fire base config
  var firebaseConfig = {
    apiKey: "AIzaSyDhzBcy71ooyvYNIyCYVsCIM97M4iOO0W8",
    authDomain: "coupon-finder-668bf.firebaseapp.com",
    projectId: "coupon-finder-668bf",
    storageBucket: "coupon-finder-668bf.appspot.com",
    messagingSenderId: "254999250241",
    appId: "1:254999250241:web:5a617106bfa38cd6728dc0"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  console.log(firebase);
}

catch(e){
  //error
  console.log(e)
}

/*
<script type="module">
  //Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.1.2/firebase-app.js";
  //TODO: Add SDKs for Firebase products that you want to use
  //https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  const firebaseConfig = {
    apiKey: "AIzaSyDhzBcy71ooyvYNIyCYVsCIM97M4iOO0W8",
    authDomain: "coupon-finder-668bf.firebaseapp.com",
    projectId: "coupon-finder-668bf",
    storageBucket: "coupon-finder-668bf.appspot.com",
    messagingSenderId: "254999250241",
    appId: "1:254999250241:web:5a617106bfa38cd6728dc0"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
</script>

*/