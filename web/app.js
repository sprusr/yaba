import GitHub from 'github-api';
//import Yaba from './yaba.js';

//const yaba = new Yaba();

window.onload = function () {
   //document.getElementById("loginBtn").onclick=test;
   document.getElementById("proposeBtn").onclick=propose;
};

function propose() {
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  var issue = document.getElementById('issue').value;
  var bounty = document.getElementById('bounty').value;

  var issueArr = issue.match(/^https?:\/\/github.com\/(.*)\/(.*)\/issues\/(.*)$/);

  //1,2,3

  var gh = new GitHub({
     username: username,
     password: password
  });

  var me = gh.getUser();

  gh.getIssues(issueArr[1], issueArr[2]).createIssueComment(issueArr[3], "hi").then(issue => {
    console.log(issue);
  });




}

// function test() {
//   username = document.getElementById('username').value;
//   password = document.getElementById('password').value;
//   githubLogin(username, password);
// }
//
// function githubLogin(username, password) {
//   // basic auth
//   var gh = new GitHub({
//      username: username,
//      password: password
//   });
//
//   var me = gh.getUser();
// }
