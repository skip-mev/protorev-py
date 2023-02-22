import json
from datetime import datetime, timedelta
from google.protobuf import any_pb2, timestamp_pb2
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins

from cosmpy.aerial.client import LedgerClient, NetworkConfig, Account
from cosmpy.aerial.wallet import LocalWallet
from cosmpy.crypto.keypairs import PrivateKey
from cosmpy.aerial.tx import Transaction as Tx, SigningCfg

from cosmpy.protos.osmosis.protorev.v1beta1.protorev_pb2 import PoolWeights
from cosmpy.protos.cosmos.authz.v1beta1.authz_pb2 import Grant, GenericAuthorization
from cosmpy.protos.cosmos.authz.v1beta1.tx_pb2 import MsgGrant, MsgExec
from cosmpy.protos.osmosis.protorev.v1beta1.tx_pb2 import MsgSetBaseDenoms
from cosmpy.protos.osmosis.protorev.v1beta1.protorev_pb2 import BaseDenom
from cosmpy.protos.osmosis.protorev.v1beta1.tx_pb2 import MsgSetHotRoutes
from cosmpy.protos.osmosis.protorev.v1beta1.protorev_pb2 import TokenPairArbRoutes, Route, Trade
from cosmpy.protos.osmosis.gamm.v1beta1.tx_pb2 import MsgSwapExactAmountIn, MsgSwapExactAmountOut
from cosmpy.protos.osmosis.poolmanager.v1beta1.swap_route_pb2 import SwapAmountInRoute, SwapAmountOutRoute
from cosmpy.protos.cosmos.base.v1beta1.coin_pb2 import Coin
from cosmpy.protos.osmosis.protorev.v1beta1.tx_pb2 import MsgSetDeveloperAccount, MsgSetMaxPoolPointsPerTx, MsgSetMaxPoolPointsPerBlock, MsgSetPoolWeights

# @DEV TODO: 
# EDIT MNEMONIC TO THE ONE YOU CREATED TO BE THE ADMIN FROM THE PREVIOUS TEST SCRIPT
ADMIN_MNEMONIC = "notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"

# @DEV TODO: 
# EDIT MNEMONIC TO BE ONE YOU HAVE ACCESS TO WITH ENOUGH FUNDS TO PAY FOR GAS
AUTHZ_EXECUTOR_MNEMONIC = "bottom loan skill merry east cradle onion journey palm apology verb edit desert impose absurd oil bubble sweet glove shallow size build burst effort"

# @DEV TODO: 
# EDIT AMOUNT TO BE A LARGE AMOUNT THE ADMIN ADDRESS HAS
# WILL SWAP THIS AMOUNT OF UOSMO INTO POOL 1
BIG_SWAP_AMOUNT = "1000000000000"

# @DEV TODO: 
# EDIT PARAMS FOR TESTNET
CHAIN_ID = "localosmosis"
DENOM = "uosmo"
ADDRESS_PREFIX = "osmo"
GAS_LIMIT = 10_000_000
GAS_FEE = "25000uosmo"
RPC_NODE = "http://0.0.0.0:26657/"
REST_NODE = "http://0.0.0.0:1317"

GRANT_MSGS = ["/osmosis.protorev.v1beta1.MsgSetDeveloperAccount", 
              "/osmosis.protorev.v1beta1.MsgSetMaxPoolPointsPerTx", 
              "/osmosis.protorev.v1beta1.MsgSetMaxPoolPointsPerBlock", 
              "/osmosis.protorev.v1beta1.MsgSetPoolWeights"]

def main():
    
    cfg = NetworkConfig(
        chain_id=CHAIN_ID,
        url=f"rest+{REST_NODE}",
        fee_minimum_gas_price=.0025,
        fee_denomination="uosmo",
        staking_denomination="uosmo",
    )
    client = LedgerClient(cfg)
    
    # Grants AUTHZ_EXECUTOR_MNEMONIC's address the ability to execute the following messages:
    # /osmosis.protorev.v1beta1.MsgSetDeveloperAccount
    # /osmosis.protorev.v1beta1.MsgSetMaxPoolPointsPerTx
    # /osmosis.protorev.v1beta1.MsgSetMaxPoolPointsPerBlock
    # /osmosis.protorev.v1beta1.MsgSetPoolWeights
    grant(client)
    
    # AUTHZ_EXECUTOR_MNEMONIC's address executes the messages above
    # MsgSetDeveloperAccount: Sets to the address of the AUTHZ_EXECUTOR_MNEMONIC
    # MsgSetMaxPoolPointsPerTx: Sets to 21
    # MsgSetMaxPoolPointsPerBlock: Sets to 200
    # MsgSetPoolWeights: Sets all to 1
    exec_granted(client)
    
    # Sets uosmo and atom as base denoms
    set_base_denoms(client)
    
    # Sets hot routes based on analysis between blocks 7400000 and 7900000
    set_hot_routes(client)
    
    # Swaps 1 million osmo into pool 1, protorev will backrun
    swap(client)
    
    
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

def create_tx(msgs: list, wallet: LocalWallet, account: Account) -> Tx:
    tx = Tx()
    for msg in msgs:
        tx.add_message(msg)
        
    tx.seal(signing_cfgs=[SigningCfg.direct(wallet.public_key(), account.sequence)], fee=GAS_FEE, gas_limit=GAS_LIMIT)
    tx.sign(wallet.signer(), CHAIN_ID, account.number)
    tx.complete()
    return tx

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

def create_grant_msg(admin_address: str, grantee: str, msg: str, expiration_delta: int) -> MsgGrant:
    authz_grant_any = create_any_msg(GenericAuthorization(msg=msg))
    expiry = timestamp_pb2.Timestamp()
    expiry.FromDatetime(datetime.now() + timedelta(days=expiration_delta))
    grant = Grant(authorization=authz_grant_any, expiration=expiry)
    msg_grant = MsgGrant(granter=admin_address, grantee=grantee, grant=grant)
    return msg_grant

def create_exec_msg(msg, grantee_address: str) -> MsgExec:
    authz_exec_any = create_any_msg(msg)
    msg_exec = MsgExec(grantee=grantee_address, msgs = [authz_exec_any])
    return msg_exec

def get_messages_to_exec(admin_address: str, executor_address: str):
    msg_set_dev_acc = MsgSetDeveloperAccount(
        admin=admin_address,
        developer_account=executor_address)
    msg_set_max_ppp_tx = MsgSetMaxPoolPointsPerTx(
        admin=admin_address,
        max_pool_points_per_tx=21)
    msg_set_max_ppp_block = MsgSetMaxPoolPointsPerBlock(
        admin=admin_address,
        max_pool_points_per_block=200)
    msg_set_pool_weights = MsgSetPoolWeights(
        admin=admin_address,
        pool_weights=PoolWeights(
            stable_weight=1,
            balancer_weight=1,
            concentrated_weight=1))
    return [msg_set_dev_acc, msg_set_max_ppp_tx, msg_set_max_ppp_block, msg_set_pool_weights]

def grant(client):
    admin_wallet, admin_address, admin_account = create_wallet(client, ADMIN_MNEMONIC)
    _, executor_address, _ = create_wallet(client, AUTHZ_EXECUTOR_MNEMONIC)
    grant_msgs = [create_grant_msg(admin_address, executor_address, msg, expiration_delta=10)
                  for msg in GRANT_MSGS]
    create_and_send_tx(grant_msgs, admin_wallet, admin_account, client, "Admin Grant")
    
def exec_granted(client):
    _, admin_address, _ = create_wallet(client, ADMIN_MNEMONIC)
    executor_wallet, executor_address, executor_account = create_wallet(client, AUTHZ_EXECUTOR_MNEMONIC)
    msgs_to_exec = get_messages_to_exec(admin_address, executor_address)
    exec_msgs = [create_exec_msg(msg=msg, grantee_address=executor_address) 
                 for msg in msgs_to_exec]
    create_and_send_tx(exec_msgs, executor_wallet, executor_account, client, "Executor Exec")
    
def set_base_denoms(client):
    admin_wallet, admin_address, admin_account = create_wallet(client, ADMIN_MNEMONIC)
    base_denom_osmo = BaseDenom(denom="uosmo", step_size="1000000")
    base_denom_atom = BaseDenom(denom="ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2", step_size="1000000")
    msg_set_base_denoms = MsgSetBaseDenoms(admin=admin_address, base_denoms=[base_denom_osmo, base_denom_atom])
    create_and_send_tx([msg_set_base_denoms], admin_wallet, admin_account, client, "Set Base Denom")

def set_hot_routes(client):
    with open("set_hot_routes_test.json") as f:
        set_hot_routes_dict = json.load(f)
    admin_wallet, admin_address, admin_account = create_wallet(client, ADMIN_MNEMONIC)
    msg_set_hot_routes = create_set_hot_routes_msg(set_hot_routes_dict, admin_address)
    create_and_send_tx([msg_set_hot_routes], admin_wallet, admin_account, client, "Set Hot Routes")

def create_set_hot_routes_msg(set_hot_routes_dict: dict, admin_address: str):
    token_pair_arb_routes_list = []
    for denom_pair, routes in set_hot_routes_dict.items():
        token_pair_arb_routes_list.append(create_token_pair_arb_routes(denom_pair, routes))
    msg_set_hot_routes = MsgSetHotRoutes(admin=admin_address, hot_routes=token_pair_arb_routes_list)
    return msg_set_hot_routes
    
def create_token_pair_arb_routes(denom_pair: str, routes: list):
    token_in, token_out = denom_pair.split("-")
    arb_routes = create_arb_routes(routes)
    token_pair_arb_routes = TokenPairArbRoutes(
        arb_routes=arb_routes,
        token_in=token_in,
        token_out=token_out)
    return token_pair_arb_routes
        
def create_arb_routes(routes: list):
    arb_routes = []
    for route in routes:
        trades = create_trades(route)
        route = Route(
            trades=trades,
            step_size="1000000")
        arb_routes.append(route)
    return arb_routes

def create_trades(route: dict):
    trades = []
    for pool_id, denoms in zip(route["route"], route["trade-denoms"]):
        token_in, token_out = denoms.split("-")
        trade = Trade(
            pool=int(pool_id),
            token_in=token_in,
            token_out=token_out)
        trades.append(trade)
    return trades
    
def swap(client):
    admin_wallet, admin_address, admin_account = create_wallet(client, ADMIN_MNEMONIC)
    swap_amount_in_route = SwapAmountInRoute(
        pool_id=1,
        token_out_denom="ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2")
    token_in = Coin(denom=DENOM, amount=BIG_SWAP_AMOUNT)
    msg_swap_exact_amount_in = MsgSwapExactAmountIn(
        sender=admin_address,
        routes=[swap_amount_in_route],
        token_in=token_in,
        token_out_min_amount="1")
    create_and_send_tx([msg_swap_exact_amount_in], admin_wallet, admin_account, client, "Swap")
    
def create_any_msg(msg):
    any_msg = any_pb2.Any()
    any_msg.Pack(msg, "")
    return any_msg
    
if __name__ == "__main__":
    main()