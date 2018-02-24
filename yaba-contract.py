from boa.blockchain.vm.Neo.Runtime import Log, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete
from boa.code.builtins import concat

def Main(operation, args):

    # The trigger determines whether this smart contract is being
    # run in 'verification' mode or 'application'

    trigger = GetTrigger()

    # 'Verification' mode is used when trying to spend assets ( eg NEO, Gas)
    # on behalf of this contract's address
    if trigger == Verification():

        return False

    # 'Application' mode is the main body of the smart contract
    elif trigger == Application():

        if operation == 'setBounty':
            if len(args) == 1:
                issue_url = args[0]
                transfer = SetBounty(issue_url)
                return transfer
            else:
                return False

        elif operation == 'revokeBounty':
            if len(args) == 1:
                issue_url = args[0]
                transfer = RevokeBounty(issue_url)
                return transfer
            else:
                return False

        elif operation == 'claimBounty':
            if len(args) == 1:
                issue_url = args[0]
                transfer = ClaimBounty(issue_url)
                return transfer
            else:
                return False

        elif operation == 'approveClaim':
            if len(args) == 2:
                issue_url = args[0]
                claimee_address = args[1]
                transfer = ApproveClaim(issue_url, claimee_address)
                return transfer
            else:
                return False

        result = 'unknown operation'

        return result

    return False


def SetBounty(issue_url):
    pass

def RevokeBounty(issue_url):
    return False # revoke disabled for now

def ClaimBounty(issue_url):
    pass

def ApproveClaim(issue_url, claimee_address):
    pass
