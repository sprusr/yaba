class Yaba {
  constructor (githubToken) {
    this.githubToken = githubToken
  }

  setBounty (issue_url, value) {
    // send transaction to neo with specified value
    let transactionHash = 'tx_hash_goes_here'
    // call github api to add comment to issue including tx hash
  }

  revokeBounty (issue_url) {
    // todo
  }

  claimBounty (issue_url) {
    // send transaction to neo with specified value
    let transactionHash = 'tx_hash_goes_here'
    // call github api to add comment to issue including tx hash
  }

  getClaims (issue_url) {
    // get all the comments from the issue_url
    // filter by which are in the claim comment format
  }

  approveClaim (issue_url, claimee_address) {
    // send transaction to neo with specified value
    let transactionHash = 'tx_hash_goes_here'
    // call github api to add comment to issue including tx hash
  }
}
