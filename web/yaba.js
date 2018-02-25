import Neon from '@cityofzion/neon-js'

class Yaba {
  constructor (githubToken, publicKey) {
    this.githubToken = githubToken
    this.publicKey = publicKey
    this.client = Neon.create.rpcClient('http://seed1.neo.org:10332', '2.3.2')
  }

  async setBounty (issue_url, value) {
    // send transaction to neo with specified value
    const sb = Neon.create.scriptBuilder()
    sb.emitAppCall('contract addr', 'setBounty', [issue_url])
    const tx = Neon.create.invocationTx(0, [], sb.str, value)
    const query = await this.client.sendRawTransaction(tx)

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

export default Yaba
