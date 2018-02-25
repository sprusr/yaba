from boa.blockchain.vm.Neo.Runtime import Log, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.code.builtins import list
from yaba.lib.storage import StorageAPI
from yaba.lib.txio import Attachments,get_asset_attachments
from boa.blockchain.vm.Neo.Output import GetValue

def Main(operation, args):

    # The trigger determines whether this smart contract is being
    # run in 'verification' mode or 'application'

    trigger = GetTrigger()

    # 'Verification' mode is used when trying to spend assets ( eg NEO, Gas)
    # on behalf of this contract's address
    if trigger == Verification():

        storage = StorageAPI()
        attachments = get_asset_attachments()

        approval_storage_location = 'claim:approval:' + attachments.sender_addr
        approval = storage.get(approval_storage_location)

        if approval == GetValue():
            storage.delete(approval_storage_location)
            return True

        return False

    # 'Application' mode is the main body of the smart contract
    elif trigger == Application():

        if operation == 'setBounty':
            if len(args) == 1:
                issue_url = args[0]
                result = SetBounty(issue_url)
                return result
            else:
                return False

        elif operation == 'revokeBounty':
            if len(args) == 1:
                issue_url = args[0]
                result = RevokeBounty(issue_url)
                return result
            else:
                return False

        elif operation == 'claimBounty':
            if len(args) == 1:
                issue_url = args[0]
                result = ClaimBounty(issue_url)
                return result
            else:
                return False

        elif operation == 'approveClaim':
            if len(args) == 2:
                issue_url = args[0]
                claimee_address = args[1]
                result = ApproveClaim(issue_url, claimee_address)
                return result
            else:
                return False

        result = 'unknown operation'

        return result

    return False


def SetBounty(issue_url):
    storage = StorageAPI()
    attachments = get_asset_attachments()

    if attachments.neo_attached == 0:
        return False

    owner_storage_location = 'issue:owner:' + issue_url
    storage.put(owner_storage_location, attachments.sender_addr)
    value_storage_location = 'issue:value:' + issue_url
    storage.put(value_storage_location, attachments.neo_attached)

    return True

def RevokeBounty(issue_url):
    return False # revoke disabled for now

def ClaimBounty(issue_url):
    attachments = get_asset_attachments()
    storage = StorageAPI()

    storage_location = 'issue:claims:' + issue_url
    bounty_claims = storage.get(storage_location)

    element_count = 1

    for c in bounty_claims:
        if c == ',':
            element_count = element_count + 1

    elements = list(length=element_count)

    current_element = 0

    for c in bounty_claims:
        if c == ',':
            current_element = current_element + 1
        else:
            elements[current_element] = elements[current_element] + c

    found = False

    for element in elements:
        if element == attachments.sender_addr:
            found = True
            break

    if not found:
        if element_count > 0:
            bounty_claims = bounty_claims + ','
        bounty_claims = bounty_claims + attachments.sender_addr
        storage.put(storage_location, bounty_claims)
        return True

    return False


def ApproveClaim(issue_url, claimee_address):
    attachments = get_asset_attachments()
    storage = StorageAPI()

    owner_storage_location = 'issue:owner:' + issue_url
    owner = storage.get(owner_storage_location)
    value_storage_location = 'issue:value:' + issue_url
    value = storage.get(value_storage_location)

    if attachments.sender_addr == owner:
        approval_storage_location = 'claim:approval:' + claimee_address
        approval = storage.put(approval_storage_location, value)

        owner_storage_location = 'issue:owner:' + issue_url
        value_storage_location = 'issue:value:' + issue_url
        claims_storage_location = 'issue:claims:' + issue_url

        storage.delete(owner_storage_location)
        storage.delete(value_storage_location)
        storage.delete(claims_storage_location)

        return  True

    return False
