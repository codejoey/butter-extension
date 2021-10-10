try {

	self.importScripts(
		'firebase/firebase-app.js',
		'firebase/firebase-database.js',
	);

	var config = {
		firebase: {
			apiKey: "xxx",
			authDomain: "xxx-xxx.firebaseapp.com",
			databaseURL: "https://xxx-xxx.firebaseio.com",
			projectId: "xxx-xxx",
			storageBucket: "xxx-d3fb9.xxx.com",
			messagingSenderId: "955042456082",
			appId: "1:xxx:web:xxx"
		}
	}

	firebase.initializeApp(config.firebase);

	chrome.runtime.onMessage.addListener((msg, sender, resp) => {

		if(msg.command == "test"){
			firebase.database().ref('test').set({
				data: "testing123"
			}).then(function() {
				resp({"status": "success", "data": "data here..."});
			}).catch(function(error) {
				resp({"status": "error", "message": error});
				console.error("Error writing document: ", error);
			});

		}
		return true;
	});
} catch(e) {
	console.log('error: ', e);
}
