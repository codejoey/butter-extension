
//test firestore...
chrome.runtime.sendMessage({command: "test"}, (response) => {
  showData(response.data);
});
