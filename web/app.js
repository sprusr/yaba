const apiKey = c66bb3467808f869596b 
const apiSecret = d3f06effa88cd1c28de113d51569201121a133d

const githubOAuth = require('github-oauth')({
    githubClient: apiKey,
    githubSecret: apiSecret,
    baseURL: 'http://localhost',
    loginURI: '/login',
    callbackURI: '/callback',
    scope: 'user' // optional, default scope is set to user 
  })
function login(){
  githubOAuth.login(req, res)
}

  githubOAuth.on('error', function(err) {
    console.error('there was a login error', err)
  })
  
  githubOAuth.on('token', function(token, serverResponse) {
    console.log('here is your shiny new github oauth token', token)
    serverResponse.end(JSON.stringify(token))
  })
  