import httpx
from google.protobuf import any_pb2
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins

from cosmpy.aerial.client import LedgerClient, NetworkConfig, Account
from cosmpy.aerial.wallet import LocalWallet
from cosmpy.crypto.keypairs import PrivateKey
from cosmpy.aerial.tx import Transaction as Tx, SigningCfg

from cosmpy.protos.cosmos.gov.v1beta1.tx_pb2 import MsgSubmitProposal, MsgVote
from cosmpy.protos.cosmos.staking.v1beta1.tx_pb2 import MsgDelegate
from cosmpy.protos.cosmos.base.v1beta1.coin_pb2 import Coin
from cosmpy.protos.osmosis.protorev.v1beta1.gov_pb2 import SetProtoRevAdminAccountProposal, SetProtoRevEnabledProposal
from cosmpy.protos.cosmos.gov.v1beta1.gov_pb2 import VoteOption

# @DEV TODO: 
# EDIT MNEMONIC TO BE ONE YOU HAVE ACCESS TO WITH LOTS OF FUNDS TO GET PROPOSALS THROUGH AND DO A BIG SWAP
# THIS ONE IS FROM LOCALOSMOSIS SETUP
MNEMONIC = "notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"

# @DEV TODO: 
# EDIT VALIDATOR ADDRESS TO BE ONE THAT CAN BE DELEGATED TO TO PASS PROPOSALS
# THIS ONE IS FROM LOCALOSMOSIS SETUP
VALIDATOR_ADDRESS = "osmovaloper12smx2wdlyttvyzvzg54y2vnqwq2qjatex7kgq4"

# @DEV TODO: 
# EDIT LARGE ENOUGH TO SINGLE HANDEDLY PASS PROPOSALS
DELEGATION_AMOUNT = "10000000000"

# @DEV TODO:
# EDIT THE MIN DEPOSIT AMOUNT FOR PROPOSALS
INITIAL_DEPOSIT_AMOUNT = "10000000"

# @DEV TODO: 
# EDIT PARAMS FOR TESTNET
CHAIN_ID = "localosmosis"
DENOM = "uosmo"
ADDRESS_PREFIX = "osmo"
GAS_LIMIT = 1_000_000
GAS_FEE = "2500uosmo"
RPC_NODE = "http://0.0.0.0:26657/"
REST_NODE = "http://0.0.0.0:1317"

def main():
    cfg = NetworkConfig(
        chain_id=CHAIN_ID,
        url=f"rest+{REST_NODE}",
        fee_minimum_gas_price=.0025,
        fee_denomination="uosmo",
        staking_denomination="uosmo",
    )
    client = LedgerClient(cfg)    
    
    # Delegates DELEGATION_AMOUNT to VALIDATOR_ADDRESS
    delegate(client)
    
    # Submits a proposal to set the admin account to MNEMONIC's and votes on it to pass
    submit_admin_account_proposal(client)
    vote_on_admin_account_proposal(client)
    
    # Submits a proposal to enable the module and votes on it to pass
    submit_enable_proposal(client)
    vote_on_enable_proposal(client)
    
def create_wallet(client, mnemonic: str) -> tuple[LocalWallet, str, Account]:
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    bip44_def_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.COSMOS).DeriveDefaultPath()
    wallet = LocalWallet(PrivateKey(bip44_def_ctx.PrivateKey().Raw().ToBytes()), prefix=ADDRESS_PREFIX)
    address = str(wallet.address())
    print(f"Address: {address}")
    account = client.query_account(address=address)
    print(f"Account: {account}")
    balance = client.query_bank_balance(address=address, denom=DENOM)
    print(f"Balance: {balance}")
    return wallet, address, account

def create_and_send_tx(msgs: list, wallet: LocalWallet, account: Account, client, print_helper) -> None:
    tx = Tx()
    for msg in msgs:
        tx.add_message(msg)
    tx.seal(signing_cfgs=[SigningCfg.direct(wallet.public_key(), account.sequence)], fee=GAS_FEE, gas_limit=GAS_LIMIT)
    tx.sign(wallet.signer(), CHAIN_ID, account.number)
    tx.complete()
    submitted_tx = client.broadcast_tx(tx)
    submitted_tx.wait_to_complete()
    print(f"{print_helper} Submitted Tx Response: {submitted_tx.response}")
    
def get_proposal_id() -> int:
    proposals = httpx.get(f"{REST_NODE}/gov/proposals").json()
    return int(proposals['result'][-1]['id'])

def delegate(client):
    new_admin_wallet, new_admin_address, new_admin_account = create_wallet(client, MNEMONIC)
    msg_delegate = MsgDelegate(
        delegator_address=new_admin_address,
        validator_address=VALIDATOR_ADDRESS,
        amount=Coin(denom=DENOM, amount=DELEGATION_AMOUNT))
    create_and_send_tx([msg_delegate], new_admin_wallet, new_admin_account, client, "Delegate")
    
def submit_admin_account_proposal(client):
    new_admin_wallet, new_admin_address, new_admin_account = create_wallet(client, MNEMONIC)
    set_admin_msg = SetProtoRevAdminAccountProposal(
        title="Set Admin Account",
        description="Set the admin account for the ProtoRev module",
        account=new_admin_address
    )
    any_set_admin_msg = create_any_msg(set_admin_msg)
    msg_proposal = MsgSubmitProposal(
        content=any_set_admin_msg,
        initial_deposit=[Coin(
            denom=DENOM,
            amount=INITIAL_DEPOSIT_AMOUNT
        )],
        proposer=new_admin_address,
        is_expedited=False
    )
    create_and_send_tx([msg_proposal], new_admin_wallet, new_admin_account, client, "Admin Account Proposal")
    
def vote_on_admin_account_proposal(client):
    new_admin_wallet, new_admin_address, new_admin_account = create_wallet(client, MNEMONIC)
    proposal_id = get_proposal_id()
    msg_vote = MsgVote(
        proposal_id=proposal_id,
        voter=new_admin_address,
        option=VoteOption.VOTE_OPTION_YES
    )
    create_and_send_tx([msg_vote], new_admin_wallet, new_admin_account, client, "Vote on Admin Account Proposal")
    
def submit_enable_proposal(client):
    wallet, address, account = create_wallet(client, MNEMONIC)
    enable_protorev_msg = SetProtoRevEnabledProposal(
        title="Set Protorev Enabled",
        description="Set the Protorev module to enabled",
        enabled=True
    )
    any_set_protorev_enabled_msg = create_any_msg(enable_protorev_msg)
    msg_proposal = MsgSubmitProposal(
        content=any_set_protorev_enabled_msg,
        initial_deposit=[Coin(
            denom=DENOM,
            amount=INITIAL_DEPOSIT_AMOUNT
        )],
        proposer=address,
        is_expedited=False
    )
    create_and_send_tx([msg_proposal], wallet, account, client, "Enable Protorev Proposal")

def vote_on_enable_proposal(client):
    wallet, address, account = create_wallet(client, MNEMONIC)
    proposal_id = get_proposal_id()
    msg_vote = MsgVote(proposal_id=proposal_id,
                       voter=address,
                       option=VoteOption.VOTE_OPTION_YES)
    create_and_send_tx([msg_vote], wallet, account, client, "Vote on Enable Protorev Proposal")
    
def create_any_msg(msg):
    any_msg = any_pb2.Any()
    any_msg.Pack(msg, "")
    return any_msg
    
if __name__ == "__main__":
    main()